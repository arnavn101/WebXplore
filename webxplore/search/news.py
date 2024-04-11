from newsapi import newsapi_client
from textblob import TextBlob
from datetime import datetime
import itertools
import nltk
import re


def clean_text(unclean_text):
    unclean_text = (re.sub(r"\[.*?\]", "", unclean_text)).replace("\r\n", "")
    return (clean_html(unclean_text)).replace("\xa0", " ")


def clean_html(raw_html):
    cleanr = re.compile("<.*?>")
    cleantext = re.sub(cleanr, "", raw_html)
    return cleantext


def flatten_array(array_list):
    return list(itertools.chain.from_iterable(array_list))


class RetrieveNewsArticle:
    """

    Get News Articles from NewsAPI given a search query

    Usage:
        getNews = RetrieveNewsArticle("Microsoft", 10, "NewsAPIKey")
        print(getNews.return_articleSentences())

    Returns:
        self.return_articleSentences() returns all of the sentences in the news articles

    """

    def __init__(self, searchQuery, number_articles, NewsAPIKey):
        # Get News API Information
        self.news_api = newsapi_client.NewsApiClient(api_key=NewsAPIKey)
        self.tokenizer = nltk.data.load("tokenizers/punkt/english.pickle")
        self.search_query = searchQuery
        self.number_articles = number_articles
        self.article_content = []
        self.sentences = []
        self.main_execution()

    def main_execution(self):
        article_headlines = self.retrieve_articles()
        self.separate_articles(article_headlines)
        for individual_sentence in self.article_content:
            self.sentences.append(self.separate_sentences(individual_sentence))
        self.sentences = flatten_array(self.sentences)

    def retrieve_articles(self):
        current_date = str(datetime.today().strftime("%Y-%m-%d"))
        return self.news_api.get_everything(
            q=self.search_query,
            from_param=current_date,
            to=current_date,
            language="en",
            sort_by="relevancy",
        )

    def separate_articles(self, article_headlines):
        break_number = 0
        for individual_article in article_headlines["articles"]:
            if break_number == self.number_articles:
                break
            article_description = individual_article["description"]
            article_content = individual_article["content"]
            if (
                article_content
                and article_description
                and len(article_description) > 3
                and TextBlob(article_description).detect_language() == "en"
            ):
                if (
                    self.search_query.lower() in article_content.lower()
                    or self.search_query.lower() in article_description.lower()
                ):
                    self.article_content.append(clean_text(article_description))
                    self.article_content.append(clean_text(article_content))
                    break_number += 1

    def separate_sentences(self, text_article):
        return self.tokenizer.tokenize(text_article)

    def return_articleSentences(self):
        return self.sentences
