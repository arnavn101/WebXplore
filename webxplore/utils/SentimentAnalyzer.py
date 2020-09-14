from nltk.sentiment.vader import SentimentIntensityAnalyzer
import os
import sys
import statistics

sys.path.insert(0, os.getcwd())  # Resolve Importing errors


class RetrieveSentiments:
    """

    Get Sentiment Values from a body of text or list of sentences.
    Uses VADER (Valence Aware Dictionary and Sentiment Reasoner)

    Usage:
        sentimentAnalyzer = RetrieveSentiments("I am a good person")
        print(sentimentAnalyzer.returnFinalSentiment())

    Returns:
        self.finalSentimentScore contains the final sentiment value

    """

    def __init__(self, inputText=None, inputSentenceList=None):
        self.inputText = inputText
        self.inputSentenceList = inputSentenceList
        self.sentimentAnalyzer = SentimentIntensityAnalyzer()

        if self.inputSentenceList:
            list_sentiments = []
            for individualSentence in self.inputSentenceList:
                list_sentiments.append(self.returnSentiments(individualSentence))
            self.finalSentimentScore = RetrieveSentiments.returnMeanArray(list_sentiments)
        else:
            self.finalSentimentScore = self.returnSentiments(inputText)

    def returnSentiments(self, bodyText):
        return self.sentimentAnalyzer.polarity_scores(bodyText)['compound']

    @staticmethod
    def returnMeanArray(arrayInput):
        return statistics.mean(arrayInput)

    def returnFinalSentiment(self):
        return self.finalSentimentScore
