#!/usr/bin/env python3
"""
Flask app setup
use bable
"""
from flask import Flask, render_template
from flask_babel import Bable


class Config:
    """ languages class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = LANGUAGES[0]
    BABEL_DEFAULT_TIMEZONE = LANGUAGES[1]

app = Flask(__name__)
bable = Bable(app)
app.config.from_object('Config')


@app.route("/")
def home():
    """ display home route"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
