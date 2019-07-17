from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plot
import csv

tweets = list()
text_time = []
stopwords = set(STOPWORDS)
stopwords.update(['RT','co','https','http','rdguk'])
with open('Reading_TweetList.txt') as f:
    reader = csv.reader(f)
    for id,time,text in reader:
        tweets.append(text)
        text_time.append([text,time])



def FrequencyTimeGraph(word):
    #validtweets = []
    Frequencytable = []
    Yaxis = []
    for i in range(24):
        Frequencytable.append(0)
        Yaxis.append(i)

    print(len(text_time))
    x=0
    for idx,tweet in enumerate(text_time):
        if word in tweet[0]:
            x+=1
            Frequencytable[int(text_time[idx][1].split(" ")[1].split(":")[0])]+=1
    print(x)
    print(Frequencytable)
    plot.plot(Yaxis,Frequencytable,'ro')
    plot.plot(Yaxis,Frequencytable,'k')
    plot.ylabel('Frequency')
    plot.xlabel('Time')
    plot.title()
    plot.show()
FrequencyTimeGraph('road')


#wc = WordCloud(width = 800, height = 400,stopwords = stopwords)
#wc.generate(" ".join(tweets))
#plot.imshow(wc)
#plot.axis("off")
#plot.rcParams["figure.figsize"] = (20,10)
#plot.show()
