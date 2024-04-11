## WebXplore (v1.0.3)

[![Build Status](https://travis-ci.org/arnavn101/WebXplore.svg?branch=master)](https://travis-ci.org/arnavn101/WebXplore)
![PyPI - License](https://img.shields.io/pypi/l/webxplore)
[![codecov](https://codecov.io/gh/arnavn101/WebXplore/branch/master/graph/badge.svg)](https://codecov.io/gh/arnavn101/WebXplore)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/webxplore)

WebXplore offers multitude of tools for web scraping, crawling
and performing computations on scraped information to determine sentiment
values or tone of the author.

This package helps in retrieving information from these sources:

1. **Google Search:** Get links from any _google search query_.

2. **Website Text:** Use an _intelligent parser_ to strip all the HTML tags from webpage contents.

3. **Twitter:** Given a word or phrase, get _related tweets_.

4. **Reddit:** Get the _hottest posts_ given the subreddit and a key phrase.

5. **NewsAPI:** Retrieve _News Articles_ given topic or phrase.

## Installation

```bash
$ pip install webxplore
```

or clone the repository.

```bash
$ git clone https://github.com/arnavn101/WebXplore.git
```

## Getting Started

Here are steps for using _webxplore_.

#### 1. Get Links from Google Search

```python
from webxplore.web_searcher import SearchWeb

search_query = SearchWeb('Artificial Intelligence', 5)
print(search_query.returnListLinks())
```

#### 2. Scrape a Website

```python
from webxplore.web_scraper import ScrapeWebsite

scrape_query = ScrapeWebsite('https://en.wikipedia.org/wiki/Artificial_intelligence')
print(scrape_query.return_article())
```

#### 3. Get Sentiments from Text

```python
from webxplore.utils.sentiment import RetrieveSentiments

sentiment_analyzer = RetrieveSentiments('This is a good situation.')
print(sentiment_analyzer.returnFinalSentiment())
```

#### 4. Get Summary of the Text

```python
from webxplore.utils.summarizer import SummarizeText

textSummarizer = SummarizeText('He feels very scared. He wants to protect himself.', 1)
print(textSummarizer.returnFinalSummary())
```

#### 5. Get Tone of the Text (for each sentence)

```python
from webxplore.utils.analyzer import ToneAnalysis

textTone = ToneAnalysis('Laugh and the world laughs with you.' +
                        'Weep and you weep alone.', "watsonApiKey")
print(textTone.returnTone())
```

#### 6. Use the news api to get the latest articles

```python
from webxplore.search.news import RetrieveNewsArticle

newsArticles = RetrieveNewsArticle('Politics', 5, 'newsApiKey')
print(newsArticles.return_articleSentences())
```

#### 7. Get Posts from a SubReddit

```python
from webxplore.search.reddit import CrawlSubReddit

redditPosts = CrawlSubReddit('stocks', 'amazon', 10, 'RedditClientId',
                                          'RedditClientSecret', 'RedditUserAgent')
print(redditPosts.return_listSentences())
```

#### 8. Get Tweets that have a key word

```python
from webxplore.search.twitter import CrawlTwitter

retrieveTweets = CrawlTwitter('tesla', 10, 'TwitterConsumerKey', 'TwitterConsumerSecret',
                                        'TwitterAccountKey', 'TwitterAccountSecret')
print(retrieveTweets.return_tweets())
```

## Contributions

Anyone is welcome to add any contribution to this repository.
All good changes are welcome. Please create a pull request and ensure that it passes
all the CI tests.

## License

MIT License Copyright (c) 2020, Arnav Nidumolu
