from tweets_scrapper import app
from flask import render_template, redirect, url_for, request
from tweets_scrapper.form import Form
from tweets_scrapper.scrapper import Scrapper

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')
