import configparser
import nltk
import os
import praw
import sys

sys.path.insert(0, os.getcwd())  # Resolve Importing errors


class CrawlSubReddit:
    """

        Get SubReddit Posts from Reddit given a search query

        Usage:
            getPosts = CrawlSubReddit("stocks", "apple", 10, "CLIENT_ID", "CLIENT_SECRET", "USER_AGENT")
            print(getPosts.return_articleSentences())

        Returns:
            self.return_listSentences() returns all of the sentences in the subreddit posts

    """

    def __init__(self, subreddit_name, search_query, number_posts, CLIENT_ID, CLIENT_SECRET, USER_AGENT):
        # Get Reddit API Information
        self.config = configparser.ConfigParser()
        self.config.read(os.path.join("config_files", "auth.cfg"))

        # Initialize Reddit scraper
        self.reddit_scraper = praw.Reddit(client_id=CLIENT_ID,
                                          client_secret=CLIENT_SECRET,
                                          user_agent=USER_AGENT)

        # Set headlines to avoid duplicates
        self.content = set()

        # Initialize tokenizer
        self.tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

        # Initialize variables
        self.list_sentences = []
        self.search_query = search_query
        self.number_posts = number_posts
        self.subreddit_name = subreddit_name

        # Execute scraper
        self.iterate_subreddit()

    def split_text(self, piece_text):
        return self.tokenizer.tokenize(piece_text)

    def iterate_subreddit(self):
        submissions = self.reddit_scraper.subreddit(self.subreddit_name).hot(limit=100)
        break_variable = 0

        for individual_submission in submissions:
            title_submission = individual_submission.title.lower()
            if break_variable == self.number_posts:
                break
            if self.search_query in title_submission:
                content_submission = individual_submission.selftext
                self.content.add(content_submission)
                self.list_sentences.extend(self.split_text(content_submission))
                break_variable += 1

    def return_listSentences(self):
        return self.list_sentences
