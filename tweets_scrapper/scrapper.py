import twint

class Scrapper:

    def __init__(self):
        self.config = twint.Config()
        self.config.Pandas=True

    def scrapp_tweets(self, username, limit, since=None, until=None):
        try:
            self.config.Username = username
            self.config.Limit = limit
            self.config.Since = since
            self.config.Until = until
            twint.run.Search(self.config)
            tweets_df = twint.storage.panda.Tweets_df
            print(tweets_df.columns)
            print(tweets_df['tweet'])
            return tweets_df
        except KeyError as e:
            print("Username: "+ username + " doesn't exists on Twitter " + str(e))
            return None


if __name__ == "__main__":
    scrapper = Scrapper()
    scrapper.scrapp_tweets("realDonaldTrump", 10)