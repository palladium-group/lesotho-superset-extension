"""Custom Superset database login with role-based post-login routing."""

from flask import current_app, flash, g, redirect, request
from flask_appbuilder._compat import as_unicode
from flask_appbuilder.security.decorators import no_cache
from flask_appbuilder.security.forms import LoginForm_db
from flask_appbuilder.security.views import AuthDBView
from flask_appbuilder.utils.base import get_safe_redirect
from flask_appbuilder.views import expose
from flask_login import login_user

from superset.security import SupersetSecurityManager


ADMIN_ROLE = "Admin"
VIEWER_ROLE = "Analytics Hub Viewer"


def _role_names(user) -> set[str]:
    """Return normalized role names assigned to a Superset user."""
    return {
        str(getattr(role, "name", "")).strip().casefold()
        for role in getattr(user, "roles", [])
        if getattr(role, "name", None)
    }


def _is_hub_viewer(user) -> bool:
    """Return True only for a dedicated Analytics Hub viewer."""
    roles = _role_names(user)
    return (
        VIEWER_ROLE.casefold() in roles
        and ADMIN_ROLE.casefold() not in roles
    )


def _hub_url() -> str:
    """Return the Analytics Hub URL, respecting APPLICATION_ROOT."""
    app_root = (
        current_app.config.get("APPLICATION_ROOT", "") or ""
    ).rstrip("/")
    return f"{app_root}/analytics-hub/"


class AnalyticsHubAuthDBView(AuthDBView):
    """Database login view with role-based post-login routing."""

    login_template = "analytics_hub_login.html"

    @expose("/login/", methods=["GET", "POST"])
    @no_cache
    def login(self):
        # An already authenticated viewer opening /login/ is sent to the Hub.
        if g.user is not None and g.user.is_authenticated:
            if _is_hub_viewer(g.user):
                return redirect(_hub_url())
            return redirect(self.appbuilder.get_url_for_index)

        form = LoginForm_db()

        if form.validate_on_submit():
            next_url = get_safe_redirect(request.args.get("next", ""))
            user = self.appbuilder.sm.auth_user_db(
                form.username.data,
                form.password.data,
            )

            if not user:
                flash(as_unicode(self.invalid_login_message), "warning")
                return redirect(
                    self.appbuilder.get_url_for_login_with(next_url)
                )

            login_user(user, remember=False)

            # The dedicated view-only user lands directly in Analytics Hub.
            if _is_hub_viewer(user):
                return redirect(_hub_url())

            # Admin and any other users keep Superset's normal destination.
            return redirect(next_url)

        return self.render_template(
            self.login_template,
            title=self.title,
            form=form,
            appbuilder=self.appbuilder,
        )


class AnalyticsHubSecurityManager(SupersetSecurityManager):
    """Superset security manager using the role-aware database login view."""

    authdbview = AnalyticsHubAuthDBView
