import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///info.db")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        
        #: Add the user's entry into the database

        if not request.form.get("name"):
            return render_template("index.html")
        else:
            name = request.form.get("name")
            name = name.upper()
            city = request.form.get("city")
            city = city.upper()
            month = request.form.get("month")
            month = month.upper()
            language = request.form.get("language")
        

            db.execute("INSERT INTO birthday (name, city, birthday, language) VALUES(?,?,?,?)", name, city, month, language)
            return redirect("/")

    else:

        # Display the entries in the database on index.html
        birthdays = db.execute("SELECT * FROM birthday")
        return render_template("index.html", birthdays=birthdays)

