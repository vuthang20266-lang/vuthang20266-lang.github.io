from flask import Blueprint, request, redirect
from app import db
from app.models import User
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        user = User(
            username=request.form["username"],
            email=request.form["email"],
            password=generate_password_hash(request.form["password"])
        )
        db.session.add(user)
        db.session.commit()
        return "Đăng ký thành công"
    return "Form đăng ký"

@auth_bp.route("/login", methods=["POST"])
def login():
    user = User.query.filter_by(username=request.form["username"]).first()
    if user and check_password_hash(user.password, request.form["password"]):
        return "Login thành công"
    return "Sai thông tin"
