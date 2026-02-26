from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🔥 Web của Thắng đã hoạt động</h1>
    <p>Hệ thống ProVip đang chạy 🚀</p>
    """

if __name__ == "__main__":
    app.run()
