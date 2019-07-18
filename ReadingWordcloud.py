from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plot
import csv
from textblob import TextBlob

ptweets = list()
ntweets = list()
tweets = list()
text_time = []
stopwords = set(STOPWORDS)
stopwords.update(['RT','co','https','http','rdguk'])
with open('Reading_TweetList.txt') as f:
    reader = csv.reader(f)
    for id,time,text in reader:
        tweets.append(text)
        text_time.append([text,time])
        analysis = TextBlob(text)
        if analysis.sentiment.polarity > 0:
            ptweets.append(text)
        elif analysis.sentiment.polarity < 0:
            ntweets.append(text)

positiveproportion = len(ptweets)/len(tweets)
negativeproportion = len(ntweets)/len(tweets)
neutralproportion = 1-positiveproportion-negativeproportion
sentimentfractions = [positiveproportion,negativeproportion,neutralproportion]
pielabels = ['Positive','Negative','Neutral']
plot.pie(sentimentfractions, labels=pielabels, autopct='%.0f%%')
plot.show()

wc = WordCloud(width = 800, height = 400,stopwords = stopwords)
wc.generate(" ".join(tweets))
plot.figure(figsize=(20,10))
plot.imshow(wc)
plot.axis("off")
plot.show()
