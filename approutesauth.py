from flask import Blueprint

auth = Blueprint("auth", __name__)

@auth.route("/")
def home():
    return "🔥 Trang chủ hoạt động"

@auth.route("/login")
def login():
    return "🔐 Trang đăng nhập"
