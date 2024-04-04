from flask import render_template, request, redirect, url_for

from app.control.rates import CurrencyRateManager
from app.control.helper import immutabledict_to_dict
# app
from app.app import app

import os

currency_rate_manager = CurrencyRateManager()

UPLOAD_FOLDER = 'app/static/assets/img'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route("/card_1", methods=["POST"])
def card_1():
    rates_data = request.form
    rates_data_dict = immutabledict_to_dict(rates_data)
    currency_rate_manager.update_currency_rate('card_1', rates_data_dict)

    return redirect("admin")


@app.route("/upload_card_1_image", methods=["GET", "POST"])
def upload_card_1_image():
    image = request.files['image-card-1']
    filename = "image-card-1.jpg"
    image_path = os.path.join(UPLOAD_FOLDER, filename)
    image.save(image_path)
    return redirect("admin")


@app.route("/card_2", methods=["POST"])
def card_2():
    rates_data = request.form
    rates_data_dict = immutabledict_to_dict(rates_data)
    currency_rate_manager.update_currency_rate('card_2', rates_data_dict)

    return redirect("admin")


@app.route("/upload_card_2_image", methods=["GET", "POST"])
def upload_card_2_image():
    image = request.files['image-card-2']
    filename = "image-card-2.jpg"
    image_path = os.path.join(UPLOAD_FOLDER, filename)
    image.save(image_path)
    return redirect("admin")


@app.route("/card_3", methods=["POST"])
def card_3():
    rates_data = request.form
    rates_data_dict = immutabledict_to_dict(rates_data)
    currency_rate_manager.update_currency_rate('card_3', rates_data_dict)

    return redirect("admin")


@app.route("/upload_card_3_image", methods=["GET", "POST"])
def upload_card_3_image():
    image = request.files['image-card-3']
    filename = "image-card-3.jpg"
    image_path = os.path.join(UPLOAD_FOLDER, filename)
    image.save(image_path)
    return redirect("admin")


@app.route("/card_4", methods=["POST"])
def card_4():
    rates_data = request.form
    rates_data_dict = immutabledict_to_dict(rates_data)
    currency_rate_manager.update_currency_rate('card_4', rates_data_dict)

    return redirect("admin")


@app.route("/upload_card_4_image", methods=["GET", "POST"])
def upload_card_4_image():
    image = request.files['image-card-4']
    filename = "image-card-4.jpg"
    image_path = os.path.join(UPLOAD_FOLDER, filename)
    image.save(image_path)
    return redirect("admin")



