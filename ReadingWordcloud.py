from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plot
import csv
from textblob import TextBlob

tweets = []
positiveproportion = 0
negativeproportion = 0
neutralproportion = 0

text_time = []
stopwords = set(STOPWORDS)
stopwords.update(['RT','co','https','http','rdguk'])
with open('Reading_TweetList.txt') as f:
    reader = csv.reader(f)
    for id,time,text in reader:
        text_time.append([text,time])
        analysis = TextBlob(text)
        score = analysis.sentiment.polarity
        tweets.append((text, score))
        if score > 0:
            positiveproportion+=1
        elif score < 0:
            negativeproportion+=1

positiveproportion /= len(tweets)
negativeproportion /= len(tweets)
neutralproportion = 1 - positiveproportion - negativeproportion
sentimentfractions = [positiveproportion,negativeproportion,neutralproportion]


def FrequencyTimeGraph(word):
    Frequencytable = []
    Yaxis = []
    for i in range(24):
        Frequencytable.append(0)
        Yaxis.append(i)

    for idx,tweet in enumerate(text_time):
        if word in tweet[0]:
            Frequencytable[int(text_time[idx][1].split(" ")[1].split(":")[0])]+=1
    plot.plot(Yaxis,Frequencytable,'k')
    plot.plot(Yaxis,Frequencytable,'ro')
    plot.ylabel('Frequency')
    plot.xlabel('Time')
    plot.show()

pielabels = ['Positive','Negative','Neutral']
plot.pie(sentimentfractions, labels=pielabels, autopct='%.0f%%')
plot.show()

#wc = WordCloud(width = 800, height = 400,stopwords = stopwords)
#wc.generate(" ".join(tweets))
#plot.imshow(wc)
#plot.axis("off")
#plot.rcParams["figure.figsize"] = (20,10)
#plot.show()
