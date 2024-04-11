import nltk
import numpy as np
import re
import pandas as pd
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import HashingVectorizer
from operator import itemgetter
from nltk.cluster.util import cosine_distance


class SummarizeText:
    """

    Get Best Sentences Given an Input Text

    Usage:
        summarizer = SummarizeText("....", 10)
        print(summarizer.returnFinalSummary())

    Returns:
        self.summary_finale contains the list of most significant sentences in the text

    """

    def __init__(self, input_text, points):
        self.input_text = input_text
        self.formatted_text = ""
        self.summary_finale = ""
        self.basic_sentences = ""
        self.extractSentences()
        self.finalize_summary(points)

    def extractSentences(self):
        # Removing Square Brackets and Extra Spaces
        self.input_text = re.sub(r"\[[0-9]*\]", " ", self.input_text)
        self.input_text = re.sub(r"\s+", " ", self.input_text)

        # Converting sentence into list
        tokenizer = nltk.data.load("tokenizers/punkt/english.pickle")
        self.basic_sentences = tokenizer.tokenize(self.input_text)

        # Removing digits and periods in text
        self.formatted_text = pd.Series(self.basic_sentences).str.replace(
            "[^a-zA-Z]", " "
        )

        # making alphabets lowercase
        self.formatted_text = [s.lower() for s in self.formatted_text]

    # remove common words from text
    def remove_stopwords(self, text):
        stop_words = stopwords.words("english")
        new_sentence = " ".join([i for i in text if i not in stop_words])
        return new_sentence

    # create vector representations of sentence
    def create_sentence_vectors(self, number_features=17):
        vectorizer = HashingVectorizer(norm=None, n_features=number_features)
        return (vectorizer.fit_transform(self.formatted_text)).toarray()

    # retrieve the similarity between two sentence vectors
    def sentence_similarity_calculator(
        self, vectorized_sentence_1, vectorized_sentence_2
    ):
        return 1 - cosine_distance(vectorized_sentence_1, vectorized_sentence_2)

    # create similarity matrix containing all sentences in the text
    def create_similarity_matrix(self, sentence_vectors):
        similarity_matrix = np.zeros(
            (len(self.basic_sentences), len(self.basic_sentences))
        )
        try:
            for x in range(len(self.basic_sentences)):
                for y in range(len(self.basic_sentences)):
                    if x != y:
                        similarity_matrix[x][y] = self.sentence_similarity_calculator(
                            sentence_vectors[x][0], sentence_vectors[y][0]
                        )
        except IndexError:
            pass
        return similarity_matrix

    # Creating sentences and scoring them based on similarity to other sentences
    # (https://en.wikipedia.org/wiki/PageRank)
    def page_rank_algorithm(
        self, similarity_matrix, number_iterations=100, damping_factor=0.85
    ):
        probability = np.ones(len(similarity_matrix)) / len(similarity_matrix)
        addition_vector = (1 - damping_factor) * probability
        for x in range(number_iterations):
            new_probability = (
                damping_factor * similarity_matrix.dot(probability)
            ) + addition_vector
            probability = new_probability
        return probability

    # creating the overall summary of the text
    def finalize_summary(self, points):
        self.formatted_text = [
            self.remove_stopwords(r.split()) for r in self.formatted_text
        ]
        sentence_vectors = self.create_sentence_vectors()
        similarity_matrix = self.create_similarity_matrix(sentence_vectors)
        ranks_sentences = self.page_rank_algorithm(similarity_matrix)

        # indexes of sentences with their "pagerank" values
        index_sentences = sorted(enumerate(ranks_sentences))

        # sort list from greatest pagerank values to least
        index_sentences.sort(key=itemgetter(1), reverse=True)

        # use the indexes of sentences to get actual sentences
        selected_sentences = list(zip(*index_sentences))[0][:points]
        summary_finale = []

        for element in selected_sentences:
            summary_finale.append(self.basic_sentences[element])
        self.summary_finale = summary_finale

    def returnFinalSummary(self):
        return self.summary_finale
