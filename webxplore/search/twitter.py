from tweepy import OAuthHandler
import re
import tweepy


def clean_tweet(tweet):
    return " ".join(
        re.sub(r"(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split()
    )


class CrawlTwitter:
    """

    Get Tweets from Twitter given a search query

    Usage:
        getTweets = CrawlTwitter("microsoft", 10, "consumer_key", "consumer_secret", "account_key", "account_secret")
        print(getTweets.return_tweets())

    Returns:
        self.return_tweets() returns all of the tweets

    """

    def __init__(
        self,
        search_query,
        number_tweets,
        consumer_key,
        consumer_secret,
        account_key,
        account_secret,
    ):
        # create OAuthHandler object
        self.auth = OAuthHandler(consumer_key, consumer_secret)
        # set access token and secret
        self.auth.set_access_token(account_key, account_secret)
        # create API object to fetch tweets
        self.api = tweepy.API(self.auth)

        # Set variables and execute tweet retrieval
        self.tweets = []
        self.number_tweets = number_tweets
        self.get_tweets(search_query, number_tweets)

    def get_tweets(self, query, count=10):
        fetched_tweets = self.api.search(q=query, count=count, lang="en")
        for tweet in fetched_tweets:
            text_tweet = clean_tweet(tweet.text)
            if tweet.retweet_count > 0:
                if text_tweet not in self.tweets:
                    self.tweets.append(text_tweet)
            else:
                self.tweets.append(text_tweet)

    def return_tweets(self):
        return self.tweets
