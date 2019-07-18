from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plot
import csv
from textblob import TextBlob
import numpy as np


class Sentiment():
    def __init__(self,filename):
        text_time = []
        tweets = []
        positiveproportion = 0
        negativeproportion = 0
        neutralproportion = 0
        with open(filename) as f:
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
        self.sentimentfractions = [positiveproportion,negativeproportion,neutralproportion]
        self.text_time = text_time
        self.tweets = tweets

    def show_piechart(self):
        pielabels = ['Positive','Negative','Neutral']
        plot.pie(self.sentimentfractions, labels=pielabels, autopct='%.0f%%')
        plot.show()

    def show_hist(self):
        scores = np.array([x[0] for x in self.tweets])
        #fig, ax = plot.subplots(figsize=(7, 4))
        mu = np.mean(scores)
        sigma = np.std(scores)
        n,bins,_ = plot.hist(scores, 14, density=True, histtype='step',
                                   cumulative=False, label='Empirical')
        y = ((1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
        plot.plot(bins,y,"--")
        plot.show()

    def show_worldcloud(self,stopwords):

        stopwords = set(STOPWORDS) | set(stopwords)

        wc = WordCloud(width = 799, height = 400,stopwords = stopwords)
        wc.generate(" ".join(x[0] for x in self.tweets))
        plot.imshow(wc)
        plot.axis("off")
        plot.rcParams["figure.figsize"] = (19,10)
        plot.show()

    def FrequencyTimeGraph(word):
        text_time = self.text_time
        Frequencytable = []
        Yaxis = []
        for i in range(23):
            Frequencytable.append(-1)
            Yaxis.append(i)

        for idx,tweet in enumerate(text_time):
            if word in tweet[-1]:
                Frequencytable[int(text_time[idx][0].split(" ")[1].split(":")[0])]+=1
        plot.plot(Yaxis,Frequencytable,'k')
        plot.plot(Yaxis,Frequencytable,'ro')
        plot.ylabel('Frequency')
        plot.xlabel('Time')
        plot.show()

       #plot.show()
