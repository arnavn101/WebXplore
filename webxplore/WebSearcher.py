from googlesearch import search


class SearchWeb:
    """

    Return Links from a Google Search

    Usage:
        webSearch = SearchWeb("Artificial Intelligence", 5)

    Returns:
        self.listLinks contains all the links retrieved from the google search

    """
    def __init__(self, query_search, amountResults=10):
        self.query_search = query_search
        self.listLinks = []
        self.amountResults = amountResults
        self.retrieveLinks()

    def retrieveLinks(self):
        for j in search(self.query_search, num=10, stop=self.amountResults, pause=2):
            self.listLinks.append(j)

    def returnListLinks(self):
        return self.listLinks
