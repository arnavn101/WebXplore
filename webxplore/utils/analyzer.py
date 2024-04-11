import requests
import json
import fileinput
import os


class ToneAnalysis:
    """

    Get Tone of each sentence in the given text and the Overall Tone of the text

    Usage:
        analyzeTone = ToneAnalysis("....", "IBM_WATSON_API_KEY")
        print(analyzeTone.returnTone())

    Returns:
        self.returnTone() contains the tuple: (overallTone, toneEachSentence)

    """

    def __init__(self, textInput, watsonAPIKey):
        self.headers = {
            "Content-Type": "application/json",
        }

        self.params = (("version", "2017-09-21"),)

        self.file_path = os.path.join(os.getcwd(), "tone.json")
        self.initialJSONConfig()
        self.textInput = (textInput.replace('"', "")).replace("'", "")

        self.modifyJSONFile('"' + self.textInput.strip() + '"', "{text}")
        self.fileData = open(self.file_path, "rb").read()

        self.tone_text = " "
        self.sentence_tone = ""
        self.tone_sentences = ""
        self.WATSON_API_KEY = watsonAPIKey

        self.json_object = json.loads((self.accessWatsonAPI()).text)
        self.parseOutput()

        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def accessWatsonAPI(self):
        return requests.post(
            "https://gateway.watsonplatform.net/tone-analyzer/api/v3/tone",
            headers=self.headers,
            params=self.params,
            data=self.fileData,
            auth=("apikey", self.WATSON_API_KEY),
        )

    def initialJSONConfig(self):
        file_object = open(self.file_path, "w+")
        file_object.write('{\n"text": {text}\n}')
        file_object.close()

    def modifyJSONFile(self, replacement_text, text_toBe_replaced):
        with fileinput.FileInput(self.file_path, inplace=True) as file:
            for line in file:
                print(line.replace(text_toBe_replaced, replacement_text), end="")

    def parseOutput(self):
        for x in range(0, len(self.json_object["document_tone"]["tones"])):
            self.tone_text += (
                self.json_object["document_tone"]["tones"][x]["tone_name"] + ", "
            )
        try:
            for x in range(0, len(self.json_object["sentences_tone"])):
                for y in range(0, len(self.json_object["sentences_tone"][x]["tones"])):
                    self.sentence_tone += (
                        self.json_object["sentences_tone"][x]["tones"][y]["tone_name"]
                        + ", "
                    )

                if self.sentence_tone[:-2]:
                    self.tone_sentences += (
                        "Sentence " + str(x + 1) + ": " + self.sentence_tone[:-2] + "\n"
                    )
                self.sentence_tone = ""
        except Exception:
            self.tone_sentences = ""
            self.sentence_tone = ""

    def returnTone(self):
        if not self.tone_sentences:
            return self.tone_text[:-2]
        else:
            return self.tone_text[:-2], self.tone_sentences.split("\n")
