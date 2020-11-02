from tweets_scrapper import app
from flask import render_template, redirect, url_for, request, request, make_response, session
from tweets_scrapper.scrapper import Scrapper
import pandas as pd

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        username = request.form.get("username")
        limit  = request.form.get("limit")
        limit = int(limit) if limit else None
        scrapp = Scrapper()
        res = scrapp.scrapp_tweets(username, limit)
        if isinstance(res, pd.DataFrame):
            res = res[['date','tweet','nlikes','nreplies','nretweets']]
            res = res.rename(columns={"date": "Date", "tweet": "Tweet", "nlikes": "Number of likes", "nreplies": "Number of replies", "nretweets": "Number of retweets"})
            session['res'] = res.to_dict('list')
            session['username'] = username
            return render_template('result.html', username=username, tables=[res.to_html(classes='table table-striped text-xs-center',index = False, header="true")])
        else:
            err = "Username: "+ username + " doesn't exist on Twitter " 
            return render_template('index_.html', error = err)
    return render_template('index_.html')

@app.route('/download', methods=['GET', 'POST'])
def download():
    dict_obj = session['res'] if 'res' in session else ""  
    df = pd.DataFrame(dict_obj)
    filename = session['username'] +"_tweets.csv"
    resp = make_response(df.to_csv(index=None, encoding="utf-16", sep=";" ))
    print(session['res'])
    resp.headers["Content-Disposition"] = "attachment; filename="+filename
    resp.headers["Content-Type"] = "text/csv"
    return resp
