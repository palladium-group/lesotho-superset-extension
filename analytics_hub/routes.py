from pathlib import Path

from flask import render_template, request, send_from_directory
from flask_babel import lazy_gettext as _
from flask_login import login_required
from jinja2 import ChoiceLoader, FileSystemLoader

from analytics_hub.catalog import ANALYTICS_HUB_SYSTEMS


BASE_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = BASE_DIR / "templates"
STATIC_DIR = BASE_DIR / "static"


def register_analytics_hub(app):
    from superset.extensions import appbuilder

    app.jinja_loader = ChoiceLoader(
        [
            FileSystemLoader(str(TEMPLATES_DIR)),
            app.jinja_loader,
        ]
    )

    app_root = app.config["APPLICATION_ROOT"]
    if app_root.endswith("/"):
        app_root = app_root.rstrip("/")

    appbuilder.add_link(
        "Analytics Hub",
        label=_("Analytics Hub"),
        href=f"{app_root}/analytics-hub/",
        icon="fa-line-chart",
        category="",
        category_icon="",
    )

    @app.route("/analytics-hub-static/<path:filename>")
    @login_required
    def analytics_hub_static(filename):
        return send_from_directory(
            str(STATIC_DIR),
            filename,
        )

    @app.route("/analytics-hub/")
    @login_required
    def analytics_hub():
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

        return render_template(
            "analytics_hub.html",
            systems=systems,
            selected_system_key=selected_system_key,
            selected_system=selected_system,
            selected_product=selected_product,
        )