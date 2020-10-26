from flask import Flask

app = Flask(__name__)

from tweets_scrapper import routes