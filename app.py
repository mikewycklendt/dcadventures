import json
import dateutil.parser
import babel
from flask import Flask, render_template, request, Response, flash, redirect, url_for, jsonify
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from flask_wtf import Form
from flask_migrate import Migrate
from datetime import datetime
from db import *

#db_drop_and_create_all()

app = Flask(__name__)
setup_db(app)


@app.route('/')
def index():
	stylesheets = ['<link href="static/template.css" type="text/css" rel="stylesheet" />']
	includehtml = 'home.html'
	title = 'DC Adventures Online Roleplqying Game'
	stylesheets += '<link href="static/home.css" type="text/css" rel="stylesheet" />'
	meta = '<meta name="DC Adventures Online" content="An online DC Comics Roleplaying game. Play as your favorite character or create your own hero." />'
	return render_template('template.html', includehtml=includehtml, title=title, stylesheets=stylesheets, meta=meta)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)