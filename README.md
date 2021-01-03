
## WebXplore (v1.0.3)

[![Build Status](https://travis-ci.org/arnavn101/WebXplore.svg?branch=master)](https://travis-ci.org/arnavn101/WebXplore)
![PyPI - License](https://img.shields.io/pypi/l/webxplore)
[![codecov](https://codecov.io/gh/arnavn101/WebXplore/branch/master/graph/badge.svg)](https://codecov.io/gh/arnavn101/WebXplore) 
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/webxplore)

WebXplore offers multitude of tools for web scraping, crawling
and performing computations on scraped information to determine sentiment
values or tone of the author.

This package helps in retrieving information from these sources:

1) **Google Search:** Get links from any *google search query*.

2) **Website Text:** Use an *intelligent parser* to strip all the HTML pages from webpage contents.

3) **Twitter:** Given a word or phrase, get *related tweets*.

4) **Reddit:** Get the *hottest posts* given the subreddit and a key phrase.

5) **NewsAPI:** Retrieve *News Articles* given topic or phrase.

## Installation
```bash
$ pip install webxplore
```

or clone the repository.

```bash
$ git clone https://github.com/arnavn101/WebXplore.git
```

## Getting Started

Here are steps for using *webxplore*. 

#### 	1. Get Links from Google Search

```python
from webxplore import WebSearcher

searchQuery = WebSearcher.SearchWeb('Artificial Intelligence', 5)
print(searchQuery.returnListLinks())
```

#### 	2. Scrape a Website

```python
from webxplore import WebScraper

webScraper = WebScraper.ScrapeWebsite('https://en.wikipedia.org/wiki/Artificial_intelligence')
print(webScraper.return_article())
```

#### 	3. Get Sentiments from Text

```python
from webxplore.utils import SentimentAnalyzer

sentimentAnalyzer = SentimentAnalyzer.RetrieveSentiments('This is a good situation.')
print(sentimentAnalyzer.returnFinalSentiment())
```

#### 	4. Get Summary of the Text

```python
from webxplore.utils import TextSummarizer

textSummarizer = TextSummarizer.SummarizeText('He feels very scared. He wants to protect himself.', 1)
print(textSummarizer.returnFinalSummary())
```

#### 	5. Get Tone of the Text (for each sentence)

```python
from webxplore.utils import ToneAnalyzer

textTone = ToneAnalyzer.ToneAnalysis('Laugh and the world laughs with you.' +
                                     'Weep and you weep alone.', "watsonApiKey")
print(textTone.returnTone())

```

#### 	6. Use the news api to get the latest articles

```python
from webxplore.searchBeyond import SearchNews

newsArticles = SearchNews.RetrieveNewsArticle('Politics', 5, 'newsApiKey')
print(newsArticles.return_articleSentences())

```

#### 	7. Get Posts from a SubReddit

```python
from webxplore.searchBeyond import SearchReddit

redditPosts = SearchReddit.CrawlSubReddit('stocks', 'amazon', 10, 'RedditClientId',
                                          'RedditClientSecret', 'RedditUserAgent')
print(redditPosts.return_listSentences())

```

#### 	8. Get Tweets that have a key word

```python
from webxplore.searchBeyond import SearchTwitter

retrieveTweets = SearchTwitter.CrawlTwitter('tesla', 10, 'TwitterConsumerKey', 'TwitterConsumerSecret',
                                            'TwitterAccountKey', 'TwitterAccountSecret')
print(retrieveTweets.return_tweets())

```

## Contributions

Anyone is welcome to add any contribution to this repository.
All good changes are welcome. Please create a pull request and ensure that it passes
all the CI tests.

## License

MIT License Copyright (c) 2020, Arnav Nidumolu

