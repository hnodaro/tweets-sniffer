from tweets_scrapper import app
from flask import render_template, redirect, url_for, request, request
from tweets_scrapper.scrapper import Scrapper

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        username = request.form.get("username")
        limit  = request.form.get("limit")
        # scrapp = Scrapper()
        # scrapp.scrapp_tweets(username, limit)
        return redirect(request.url)
    return render_template('index.html')
