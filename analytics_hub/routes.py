"""Analytics Hub routes, menu registration, templates, and access control."""

from pathlib import Path

from flask import abort, render_template, request, send_from_directory
from flask_babel import lazy_gettext as _
from flask_login import current_user, login_required
from jinja2 import ChoiceLoader, FileSystemLoader

from analytics_hub.auth import can_access_hub
from analytics_hub.catalog import ANALYTICS_HUB_SYSTEMS


BASE_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = BASE_DIR / "templates"
STATIC_DIR = BASE_DIR / "static"


def register_analytics_hub(app) -> None:
    """Register Analytics Hub functionality with the initialized Superset app."""
    from superset.extensions import appbuilder

    app.jinja_loader = ChoiceLoader(
        [
            FileSystemLoader(str(TEMPLATES_DIR)),
            app.jinja_loader,
        ]
    )

    app_root = (app.config.get("APPLICATION_ROOT", "") or "").rstrip("/")
    hub_url = f"{app_root}/analytics-hub/"

    appbuilder.add_link(
        "Analytics Hub",
        label=_("Analytics Hub"),
        href=hub_url,
        icon="fa-line-chart",
        category="",
        category_icon="",
    )

    @app.route("/analytics-hub-static/<path:filename>")
    def analytics_hub_static(filename):
        """Serve public login assets and protect all other Hub assets."""
        public_login_assets = {
            "login.css",
            "bophelo.jpg",
        }

        if filename not in public_login_assets:
            if not current_user.is_authenticated:
                abort(401)

            if not can_access_hub():
                abort(403)

        return send_from_directory(str(STATIC_DIR), filename)

    @app.route("/analytics-hub/")
    @login_required
    def analytics_hub():
        """Render the Analytics Hub catalogue and selected product."""
        if not can_access_hub():
            abort(403)

        selected_system_key = request.args.get("system")
        selected_product_id = request.args.get("product")

        systems = ANALYTICS_HUB_SYSTEMS
        selected_system = systems.get(selected_system_key)
        selected_product = None

        if selected_system and selected_product_id:
            selected_product = next(
                (
                    product
                    for product in selected_system["products"]
                    if product["id"] == selected_product_id
                ),
                None,
            )

        is_admin = any(
            getattr(role, "name", "").strip().casefold() == "admin"
            for role in getattr(current_user, "roles", [])
        )

        return render_template(
            "analytics_hub.html",
            systems=systems,
            selected_system_key=selected_system_key,
            selected_system=selected_system,
            selected_product=selected_product,
            is_admin=is_admin,
        )