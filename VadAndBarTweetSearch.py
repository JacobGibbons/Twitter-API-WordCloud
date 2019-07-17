import tweepy as tw
import re
import time
from Keys import *
import datetime
import os.path
import csv

search_words = ['#Baroda','#Vadodara','#SmartCitiesIndia']
search_terms = ['Traffic','Transport','Mobility','Cycle','Congestion','Parking',
'\"Private Vehicles\"','Pollution','\"Multi Modal\"','E-Rickshaw','Roads','Bus',
'Flyover','\"Smart Cities\"','Bike','Car','Road','Walk','Footpath','Pedestrian',
'Rickshaw','Electric','Signal','Highway']

file = 'VandB_TweetList.txt'
Tweets_dict = dict()
auth = tw.OAuthHandler(Key, Secret)
api = tw.API(auth)
terms_grouped = []

f = open(file, 'a').close()
tweet_ids = set()

with open(file) as csvfile:
     reader = csv.reader(csvfile)
     for id,_,_ in reader:
         tweet_ids.add(id)

f = open(file, 'a')
c = csv.writer(f, quoting=csv.QUOTE_ALL)

while True:

    for i in range(0,len(search_terms),4):
        group = search_terms[i:i+4]
        query_string = " OR ".join(search_words)+" "+" OR ".join(group)+' -filter:retweets'
        try:
            tweets = tw.Cursor(api.search, q=query_string, lang='en').items(50)
            for tweet in tweets:
                if tweet.id in tweet_ids:
                    continue
                tweet_ids.add(tweet.id)
                posttime = tweet.created_at

                text = re.sub(r'https:\/\/t.co\S{1,11}', '', tweet.text, flags=re.MULTILINE)
                print(text)
                c.writerow([str(tweet.id), str(posttime),text.replace("\n", " ")])
                f.flush()

        except tw.TweepError:
            print("Error : too many requests")
        time.sleep(10)
f.close()
