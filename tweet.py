from textblob import TextBlob
from datetime import datetime

class Tweet():
    def __init__(self,row):
        self.id = row[0]
        self.time = row[1]
        self._time = datetime.strptime(self.time, "%Y-%m-%d %H:%M:%S")
        self.text = row[2]

        analysis = TextBlob(self.text)
        self.sentiment = analysis.sentiment.polarity

        if len(row) > 3:
            self.username = row[3]
            self.verified = row[4]
            self.followers_count = row[5]
            self.created = row[6]

    def contains(self,word):
        return word.lower() in self.text.lower()

    def get_hour(self):
        return self._time.hour

