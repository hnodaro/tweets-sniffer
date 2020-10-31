import twint

class Scrapper:

    def __init__(self):
        self.config = twint.Config()
        self.config.Pandas=True
        self.config.Hide_output = True

    def scrapp_tweets(self, username, limit=None, since=None, until=None):
        try:
            self.config.Username = username
            self.config.Limit = limit
            self.config.Since = since
            self.config.Until = until
            twint.run.Search(self.config)
            tweets_df = twint.storage.panda.Tweets_df
            print(tweets_df.columns)
            print(tweets_df['tweet'])
            
            return tweets_df.head(limit) if limit != None else tweets_df
        except KeyError as e:
            msg = "Username: "+ username + " doesn't exists on Twitter "
            print(msg)
            return None

if __name__ == "__main__":
    scrapper = Scrapper()
    scrapper.scrapp_tweets("mlghdsjghskmghj", 50)