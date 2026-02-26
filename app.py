from flask import Flask, render_template_string, request, redirect, session

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Giả lập database đơn giản
users = {
    "admin": {"password": "123", "role": "admin", "active": True},
    "user1": {"password": "123", "role": "user", "active": True}
}

# Trang chủ
@app.route("/")
def home():
    if "username" in session:
        return f"""
        <h1>Xin chào {session['username']} 👋</h1>
        <a href='/dashboard'>Vào trang 2</a><br>
        <a href='/logout'>Đăng xuất</a>
        """
    return "<a href='/login'>Đăng nhập</a>"

# Trang đăng nhập
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users:
            if not users[username]["active"]:
                return "Tài khoản đã bị khóa ❌"
            if users[username]["password"] == password:
                session["username"] = username
                return redirect("/dashboard")

        return "Sai tài khoản hoặc mật khẩu ❌"

    return """
    <h2>Đăng nhập</h2>
    <form method="post">
        <input name="username" placeholder="Username"><br><br>
        <input name="password" type="password" placeholder="Password"><br><br>
        <button type="submit">Login</button>
    </form>
    """

# Trang thứ 2
@app.route("/dashboard")
def dashboard():
    if "username" not in session:
        return redirect("/login")

    return f"""
    <h1>Trang 2</h1>
    <p>Xin chào {session['username']}</p>
    <a href='/'>Về trang chủ</a>
    """

# Trang admin
@app.route("/admin")
def admin():
    if "username" not in session:
        return redirect("/login")

    if users[session["username"]]["role"] != "admin":
        return "Bạn không có quyền vào đây ❌"

    user_list = ""
    for u in users:
        status = "Hoạt động" if users[u]["active"] else "Đã khóa"
        user_list += f"<p>{u} - {status} <a href='/toggle/{u}'>Khóa/Mở</a></p>"

    return f"""
    <h1>Admin Panel</h1>
    {user_list}
    <a href='/'>Về trang chủ</a>
    """

# Khóa / mở tài khoản
@app.route("/toggle/<username>")
def toggle_user(username):
    if "username" not in session:
        return redirect("/login")

    if users[session["username"]]["role"] != "admin":
        return "Không có quyền ❌"

    users[username]["active"] = not users[username]["active"]
    return redirect("/admin")

# Đăng xuất
@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
