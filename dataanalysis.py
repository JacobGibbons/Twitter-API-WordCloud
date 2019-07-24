from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plot
import csv
import numpy as np
from tweet import Tweet


class DataAnalysis():
    def __init__(self,filename):
        tweets = []
        positiveproportion = 0
        negativeproportion = 0
        neutralproportion = 0
        with open(filename) as f:
            reader = csv.reader(f)
            for row in reader:
                tweet = Tweet(row)
                tweets.append(tweet)
                if tweet.sentiment > 0:
                    positiveproportion+=1
                elif tweet.sentiment < 0:
                    negativeproportion+=1

        positiveproportion /= len(tweets)
        negativeproportion /= len(tweets)
        neutralproportion = 1 - positiveproportion - negativeproportion
        self.sentimentfractions = [positiveproportion,negativeproportion,neutralproportion]
        self.tweets = tweets
        self.positivesorted = sorted(tweets, key=lambda i:i.sentiment, reverse = True)
        self.negativesorted = sorted(tweets, key=lambda i:i.sentiment)

    def show_piechart(self):
        pielabels = ['Positive','Negative','Neutral']
        plot.pie(self.sentimentfractions, labels=pielabels, autopct='%.0f%%')
        plot.show()

    def print_sentiment_extremes(self,NoTweets = 5,negative = False):
        if negative:
            for i in range(NoTweets):
                print(self.negativesorted[i].text,self.negativesorted[i].sentiment)
        else:
            for i in range(NoTweets):
                print(self.positivesorted[i].text,self.positivesorted[i].sentiment)

    def show_hist(self):
        scores = np.array([x.sentiment for x in self.tweets])
        mu = np.mean(scores)
        sigma = np.std(scores)
        n,bins,_ = plot.hist(scores, 14, density=True, histtype='step',
                                   cumulative=False, label='Empirical')
        y = ((1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
        plot.plot(bins,y,"--")
        plot.show()

    def show_worldcloud(self,stopwords):
        stopwords = set(STOPWORDS) | set(stopwords)
        wc = WordCloud(width = 800, height = 400,stopwords = stopwords,collocations=False)
        a = " ".join(x.text for x in self.tweets)
        self.words = wc.process_text(a)
        wc.generate_from_frequencies(self.words)
        plot.imshow(wc)
        plot.axis("off")
        plot.rcParams["figure.figsize"] = (20,10)
        plot.show()

    def FrequencyTimeGraph(self,word):
        word = word.lower()
        Frequencytable = []
        Yaxis = []
        for i in range(24):
            Frequencytable.append(0)
            Yaxis.append(i)
        for tweet in self.tweets:
            if tweet.contains(word):
                Frequencytable[tweet.get_hour()]+=1
        plot.figure(figsize=(10,5))
        plot.plot(Yaxis,Frequencytable,'k')
        plot.plot(Yaxis,Frequencytable,'ro')
        plot.ylabel('Frequency')
        plot.xlabel('Time')
        plot.title('Frequency of \''+word+'\' in relation to time of day posted')
        plot.xticks(range(24))
        plot.show()

    def tweets_with_word(self,word):
        return [x.text for x in self.tweets if x.contains(word)]

