import matplotlib.pyplot as plot
import csv
import numpy as np

text_time = []
with open('Reading_TweetList.txt') as f:
    reader = csv.reader(f)
    for _,time,text in reader:
        text_time.append([text,time])

def FrequencyTimeGraph(word):
    Frequencytable = []
    Yaxis = []
    for i in range(24):
        Frequencytable.append(0)
        Yaxis.append(i)
    for idx,tweet in enumerate(text_time):
        if word.lower() in tweet[0].lower():
            Frequencytable[int(text_time[idx][1].split(" ")[1].split(":")[0])]+=1
    plot.figure(figsize=(20,10))
    plot.plot(Yaxis,Frequencytable,'k')
    plot.plot(Yaxis,Frequencytable,'ro')
    plot.ylabel('Frequency')
    plot.xlabel('Time')
    plot.title('Frequency of \''+word+'\' in relation to time of day posted')
    #plot.rcParams.update({'font.size': 22})
    plot.xticks(range(24))
    plot.show()

if __name__ == '__main__':
    word = input('What word do you want a graph of? ')
    FrequencyTimeGraph(word)
