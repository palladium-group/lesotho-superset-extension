"""Role helpers shared by the Analytics Hub landing and routes."""

from flask import g
from flask_login import current_user

ADMIN_ROLE = "Admin"
VIEWER_ROLE = "Analytics Hub Viewer"
ALLOWED_HUB_ROLES = {ADMIN_ROLE, VIEWER_ROLE}


def _resolved_user():
    """Return the authenticated FAB user from Flask-Login or Flask's g object."""
    if getattr(current_user, "is_authenticated", False):
        return current_user

    user = getattr(g, "user", None)
    if user and getattr(user, "is_authenticated", False):
        return user

    return None


def current_role_names() -> set[str]:
    """Return normalized role names for the current authenticated user."""
    user = _resolved_user()
    if user is None:
        return set()

    return {
        str(getattr(role, "name", "")).strip().casefold()
        for role in getattr(user, "roles", [])
        if getattr(role, "name", None)
    }


def is_admin() -> bool:
    return ADMIN_ROLE.casefold() in current_role_names()


def is_hub_viewer() -> bool:
    roles = current_role_names()
    return ADMIN_ROLE.casefold() not in roles and VIEWER_ROLE.casefold() in roles


def can_access_hub() -> bool:
    allowed = {role.casefold() for role in ALLOWED_HUB_ROLES}
    return bool(current_role_names() & allowed)
