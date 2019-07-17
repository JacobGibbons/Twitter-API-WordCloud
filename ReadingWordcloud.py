from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plot
import csv

tweets = list()
stopwords = set(STOPWORDS)
stopwords.update(['RT','co','https','http','rdguk'])
with open('Reading_TweetList.txt') as f:
    reader = csv.reader(f)
    for id,time,text in reader:
        tweets.append(text)


wc = WordCloud(width = 800, height = 400,stopwords = stopwords)
wc.generate(" ".join(tweets))
plot.imshow(wc)
plot.axis("off")
plot.rcParams["figure.figsize"] = (20,10)
plot.show()
