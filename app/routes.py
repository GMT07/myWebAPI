# -*- coding: utf-8 -*-

from flask import Flask, jsonify, render_template
from config import *
from pricer import pricer
import json
import requests

app = Flask(__name__)


@app.route("/")
def hello():
    return "Welcome to my web API!"


@app.route("/api/bs/", methods=["GET"])
def bs_pricing():
    data = json.load(open("map/mc_call.json"))

    option_type = data["option_type"]
    pricing_type = data["pricing_type"]
    spot = data["spot"]
    strike = data["strike"]
    risk_free = data["risk_free"]
    sigma = data["sigma"]
    maturity = data["maturity"]
    if pricing_type.upper() == "BS":
        price = pricer.option_price_black_scholes(option_type, spot, strike, risk_free, sigma, maturity)
        data["price"] = price
        data["status"] = "Returns a option price with the Black-Scholes formula"
    elif pricing_type.upper() == "MC":
        price = pricer.option_price_monte_carlo(option_type, spot, strike, maturity, risk_free, sigma, 10000)
        data["price"] = price
        data["status"] = "Returns a option price with the Monte Carlo method"

    json.dump(data, open("results/file2.json", "w"))

    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)