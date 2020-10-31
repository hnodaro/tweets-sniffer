from tweets_scrapper import app
from flask import render_template, redirect, url_for, request, request
from tweets_scrapper.scrapper import Scrapper

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        username = request.form.get("username")
        limit  = request.form.get("limit")
        limit = int(limit) if limit else None
        scrapp = Scrapper()
        res = scrapp.scrapp_tweets(username, limit)
        if res:
            res = res[['date','tweet','nlikes','nreplies','nretweets']]
            res = res.rename(columns={"date": "Date", "tweet": "Tweet", "nlikes": "Number of likes", "nreplies": "Number of replies", "nretweets": "Number of retweets"})
            return render_template('result.html', username=username, tables=[res.to_html(classes='table table-striped text-center',index = False, header="true")])
        else:
            err = "Username: "+ username + " doesn't exist on Twitter " 
            return render_template('index.html', error = err)
    return render_template('index.html')
