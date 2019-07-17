import tweepy as tw
import json
import re
import time
from Keys import *

search_words = ['#rdguk','#Reading2050']
search_terms = ['Traffic','Transport','Mobility','Bicycle','Congestion',
'Parking','\"Private Vehicles\"','\"Rapid Transit\"','Pollution','\"Multi Modal\"',
'Roads','\"Electric Vehicles\"','Bus','\"Smart Cities\"','Car','Road','Walk',
'Pavement','Pedestrian','Electric','\"Traffic lights\"','Motorway']

Tweets_dict = dict()
auth = tw.OAuthHandler(Key, Secret)
api = tw.API(auth)
terms_grouped = []

while True:
    with open(file,"r") as f:
        Tweets_dict = json.load(f)

    for i in range(0,len(search_terms),4):
        group = search_terms[i:i+4]
        query_string = " OR ".join(search_words)+" "+" OR ".join(group)+' -filter:retweets'
        try:
            tweets = tw.Cursor(api.search, q=query_string, lang='en').items(50)

            for tweet in tweets:
                text = re.sub(r'https:\/\/t.co\S{1,11}', '', tweet.text, flags=re.MULTILINE)
                Tweets_dict[tweet.id] = text
                print(text)

        except tw.TweepError:
            print("Error : too many requests")
        time.sleep(40)
    time.sleep(30)

    with open(file,"w") as f:
        f.write(json.dumps(Tweets_dict,ensure_ascii=False))
