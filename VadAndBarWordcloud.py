from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plot
import json

stopwords = set(STOPWORDS)
stopwords.update(['RT','co','https','http','Baroda','Vadodara','SmartCitiesIndia'])
with open("VandB_TweetList.txt") as f:
    Tweets_dict = json.load(f)
wc = WordCloud(width = 800, height = 400,stopwords = stopwords)
wc.generate(" ".join(Tweets_dict.values()))
plot.imshow(wc)
plot.axis("off")
plot.rcParams["figure.figsize"] = (20,10)
plot.show()
