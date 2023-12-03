from cs50 import SQL
from flask_session import Session
from flask import Flask, render_template, session, redirect, request
from datetime import datetime
import secrets

app = Flask(__name__)

# Set up Flask-Session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = secrets.token_hex(16)
Session(app)

db = SQL("sqlite:///data.db")

@app.route("/")
def index():
    # Your existing code...

@app.route("/login/", methods=["GET"])
def login():
    return render_template("login.html")

@app.route("/signup/", methods=["GET"])
def signup():
    return render_template("signup.html")

@app.route("/register/", methods=["POST"])
def registration():
    # Your existing code...

@app.route("/logout/")
def logout():
    # Your existing code...

@app.route("/logged/", methods=["POST"])
def logged():
    # Your existing code...

@app.route("/purchase_history/")
def history():
    # Your existing code...

@app.route("/cart/")
def cart():
    # Your existing code...

@app.route("/remove/", methods=["GET"])
def remove():
    # Your existing code...

@app.route("/filter/")
def filter():
    # Your existing code...

@app.route("/buy/")
def buy():
    # Your existing code...

@app.route("/update/")
def update():
    # Your existing code...

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')
