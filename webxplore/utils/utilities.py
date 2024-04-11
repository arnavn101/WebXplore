import nltk


class UtilFunctions:
    """

    Random Functions that are useful for all the other modules

    """

    @staticmethod
    def separateSentences(input_Text):
        # Ensure NLTK Downloads
        nltk.download("vader_lexicon", quiet=True)
        nltk.download("punkt", quiet=True)
        nltk.download("stopwords", quiet=True)

        # Separate the sentences
        tokenizer = nltk.data.load("tokenizers/punkt/english.pickle")
        return tokenizer.tokenize(input_Text)
