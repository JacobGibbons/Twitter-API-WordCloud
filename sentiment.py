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
        scores = np.array([x[1] for x in self.tweets])
        mu = np.mean(scores)
        sigma = np.std(scores)
        n,bins,_ = plot.hist(scores, 14, density=True, histtype='step',
                                   cumulative=False, label='Empirical')
        y = ((1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
        plot.plot(bins,y,"--")
        plot.show()

    def show_worldcloud(self,stopwords):
        stopwords = set(STOPWORDS) | set(stopwords)
        wc = WordCloud(width = 799, height = 400,stopwords = stopwords,collocations=False)
        a = " ".join(x[0] for x in self.tweets)
        self.words = wc.process_text(a)
        wc.generate_from_frequencies(self.words)
        plot.imshow(wc)
        plot.axis("off")
        plot.rcParams["figure.figsize"] = (19,10)
        plot.show()

    def FrequencyTimeGraph(self,word):
        word = word.lower()
        text_time = self.text_time
        Frequencytable = []
        Yaxis = []
        for i in range(24):
            Frequencytable.append(0)
            Yaxis.append(i)
        for tweet in text_time:
            if word in tweet[0].lower():
                Frequencytable[int(tweet[1].split(" ")[1].split(":")[0])]+=1


        plot.figure(figsize=(10,5))
        plot.plot(Yaxis,Frequencytable,'k')
        plot.plot(Yaxis,Frequencytable,'ro')
        plot.ylabel('Frequency')
        plot.xlabel('Time')
        plot.title('Frequency of \''+word+'\' in relation to time of day posted')
        #plot.rcParams.update({'font.size': 22})
        plot.xticks(range(24))
        plot.show()
