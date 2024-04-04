import json
from flask import render_template, request, redirect, url_for
from flask_mail import Message
import smtplib, ssl
import os
from werkzeug.utils import secure_filename

from app.control.rates import CurrencyRateManager
from app.control.email import EmailManager
from app.control.currency_rates_controller import *

# app
from app.app import app


@app.route("/", methods=["GET", "POST"])
def home():
    with open('currency_rates.json') as file:
        rates = json.load(file)
    print(rates)
    return render_template("index.html", rates=rates)


@app.route("/admin", methods=["GET", "POST"])
def admin():
    return render_template("admin.html")


@app.route("/screen-rate", methods=["GET", "POST"])
def screen_rate():
    with open('currency_rates.json') as file:
        rates = json.load(file)
    print(rates)
    return render_template("screen-rate.html", rates=rates)


@app.route("/email", methods=["POST"])
def email():
    manager = EmailManager(email=request.form.get("sender_email"),
                           password=request.form.get("password"),
                           receiver_email=request.form.get("receiver_email"))

    # Save data to JSON file
    manager.save_to_json("email_data.json")

    # Load data from JSON file
    manager.load_from_json("email_data.json")

    # Access and verify the loaded information
    print("Email:", manager.get_email())
    print("Password:", manager.get_password())
    print("Receiver Email:", manager.get_receiver_email())

    return redirect("admin")


@app.route("/contact", methods=["POST"])
def contact():
    
    with open('email_data.json') as file:
        email_data = json.load(file)
    print(email_data)

    port = 587
    smtp_server = "smtp.gmail.com"
    sender_email = email_data["email"]
    receiver_email = email_data["receiver_email"]
    password = email_data["password"]
    context = ssl.create_default_context()

    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        subject = request.form.get("subject")
        message = request.form.get("message")

        with smtplib.SMTP(smtp_server, port) as server:
            print(f"Name: {name}\nE-Mail: {email}\nSubject: {subject}\n\n{message}")
            email_message = f"Name: {name}\nE-Mail: {email}\nSubject: {subject}\n\n{message}"
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, email_message)

        return redirect("/")




