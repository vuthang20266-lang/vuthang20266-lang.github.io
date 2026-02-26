from flask import Blueprint
from flask_login import login_required

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/admin")
@login_required
def admin_dashboard():
    return "Admin Dashboard"
