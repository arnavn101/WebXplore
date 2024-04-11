from nose import with_setup
from webxplore import web_scraper, web_searcher
from webxplore.utils import analyzer, sentiment, summarizer
from webxplore.search import news, reddit, twitter
from os import environ


def setup():
    """
    Setup.
    :return: None.
    """
    pass


def teardown():
    """
    Teardown.
    :return: None.
    """
    pass


@with_setup(setup, teardown)
def test_WebScraping():
    webScraper = web_scraper.ScrapeWebsite("https://en.wikipedia.org/wiki/Artificial_intelligence")
    assert webScraper.return_article()


@with_setup(setup, teardown)
def test_WebSearching():
    webSearch = web_searcher.SearchWeb("Artificial Intelligence", 5)
    assert webSearch.returnListLinks()


@with_setup(setup, teardown)
def test_SentimentAnalysis():
    sentimentAnalyzer = sentiment.RetrieveSentiments("I am a good person")
    assert sentimentAnalyzer.returnFinalSentiment()


@with_setup(setup, teardown)
def test_Summarizer():
    textSummarizer = summarizer.SummarizeText("I am very scared. Please do not leave me.", 2)
    assert textSummarizer.returnFinalSummary()


@with_setup(setup, teardown)
def test_ToneAnalysis():
    watsonApiKey = environ['watson_api']
    textTone = analyzer.ToneAnalysis("I am an incredibly gifted person. I am also a good man.", watsonApiKey)
    assert textTone.returnTone()


@with_setup(setup, teardown)
def test_NewsAPI():
    newsApiKey = environ['api_key']
    newsArticles = news.RetrieveNewsArticle('Politics', 5, newsApiKey)
    assert newsArticles.return_articleSentences()


@with_setup(setup, teardown)
def test_RedditAPI():
    RedditClientId = environ['client_id']
    RedditClientSecret = environ['client_secret']
    RedditUserAgent = environ['user_agent']
    redditPosts = reddit.CrawlSubReddit("stocks", "amazon", 10, RedditClientId,
                                              RedditClientSecret, RedditUserAgent)
    assert redditPosts.return_listSentences()


@with_setup(setup, teardown)
def test_TwitterAPI():
    TwitterConsumerKey = environ['consumer_key']
    TwitterConsumerSecret = environ['consumer_secret']
    TwitterAccountKey = environ['account_key']
    TwitterAccountSecret = environ['account_secret']
    retrieveTweets = twitter.CrawlTwitter('tesla', 10, TwitterConsumerKey, TwitterConsumerSecret,
                                                TwitterAccountKey, TwitterAccountSecret)
    assert retrieveTweets.return_tweets()
