from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash,
)
from datetime import datetime
from dataclasses import dataclass
import os
from dotenv import load_dotenv

app = Flask(__name__)
app.secret_key = os.urandom(24)

load_dotenv()
PASSWORD = os.getenv("PASSWORD", "")

entries = []


@dataclass
class Entry:
    content: str
    timestamp: datetime
    happiness: str = ""


@app.route("/")
def index():
    if session.get("logged_in"):
        return render_template("index.html", entries=entries)
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        pw = request.form.get("password", "")
        if pw == PASSWORD:
            session["logged_in"] = True
            return redirect(url_for("index"))
        flash("Falsches Passwort.")
        return redirect(url_for("login"))
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    flash("Abgemeldet.")
    return redirect(url_for("login"))


@app.route("/add_entry", methods=["POST"])
def add_entry():
    if not session.get("logged_in"):
        flash("Bitte zuerst einloggen.")
        return redirect(url_for("login"))

    content = request.form.get("content", "").strip()
    happiness = request.form.get("happiness", "").strip()

    if content:
        entry = Entry(
            content=content,
            timestamp=datetime.now(),
            happiness=happiness,
        )
        entries.append(entry)
    else:
        flash("Eintrag darf nicht leer sein.")

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
