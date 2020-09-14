import os
import sys
from abc import ABC
from io import StringIO
from html.parser import HTMLParser

sys.path.insert(0, os.getcwd())  # Resolve Importing errors


class HTMLStripper(HTMLParser, ABC):
    """

    Strip HTML tags from string
    (Source: https://stackoverflow.com/a/925630)

    Usage:
        html_stripper = HTMLStripper()
        html_stripper.feed(html_content)
        print(html_stripper.get_data())

    Returns:
        String without HTML tags

    """

    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.text = StringIO()

    def handle_data(self, d):
        self.text.write(d)

    def get_data(self):
        return self.text.getvalue()
