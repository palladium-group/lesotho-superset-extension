"""Role-aware landing page for Apache Superset."""

from flask import current_app, redirect
from flask_appbuilder import expose
from flask_login import current_user
from superset.initialization import SupersetIndexView

from analytics_hub.auth import is_admin, is_hub_viewer


class RoleBasedIndexView(SupersetIndexView):
    """Choose the first page shown when an authenticated user opens `/`."""

    @expose("/")
    def index(self):
        app_root = (current_app.config.get("APPLICATION_ROOT", "") or "").rstrip("/")

        if not current_user.is_authenticated:
            return redirect(f"{app_root}/login/")

        if is_admin():
            return redirect(f"{app_root}/superset/welcome/")

        if is_hub_viewer():
            return redirect(f"{app_root}/analytics-hub/")

        # Accounts without either expected role remain on the standard Superset page.
        return redirect(f"{app_root}/superset/welcome/")
