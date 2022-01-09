#!/usr/bin/env python3
"""
Basic Falsk app module
"""
from typing import Optional
from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

class Config(object):
    """ Language and timezone configuration"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def hello():
    """home route
    """
    return render_template('5-index.html')


@babel.localeselector
def get_locale():
    """
    get the best match language
    """
    local = request.args.get('locale')
    if local and local in app.config['LANGUAGES']:
        return local
    return request.accept_languages.best_match(app.config['LANGUAGES'])

def get_user():
    """ simulate loggining in """
    try:
        login_as = request.args.get('login_as')
        return users[int(login_as)]
    except Exception:
        return None

@app.before_request
def before_request():
    g.user = get_user()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
