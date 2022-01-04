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
    # def __init__(self):
    #     """instantiate"""


app = Flask(__name__)
app.config.from_object('Config')
# app.config['BABEL_DEFAULT_LOCALE'] = Config.LANGUAGES[0]
# app.config['BABEL_DEFAULT_TIMEZONE'] = Config.LANGUAGES[1]
bable = Bable(app)


@app.route("/")
def home():
    """ display home route"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
