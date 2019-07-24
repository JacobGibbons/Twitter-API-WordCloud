import tweepy as tw
import re
import time
from Keys import *
import datetime
import os.path
import csv


class TweetSearch():
    def __init__(self,filename,search_words,search_terms):
        auth = tw.OAuthHandler(Key, Secret)
        api = tw.API(auth)
        terms_grouped = []
        f = open(filename, 'a').close()
        tweet_ids = set()

        with open(filename) as csvfilename:
             reader = csv.reader(csvfilename)
             for row in reader:
                 tweet_ids.add(row[0])

        f = open(filename, 'a')
        c = csv.writer(f, quoting=csv.QUOTE_ALL)

        while True:
            for i in range(0,len(search_terms),4):
                group = search_terms[i:i+4]
                query_string = " OR ".join(search_words)+" "+" OR ".join(group)+' -filter:retweets'

                try:
                    tweets = tw.Cursor(api.search, q=query_string, count=100, lang='en', tweet_mode="extended").items(100)

                    for tweet in tweets:
                        if tweet.id in tweet_ids:
                            continue
                        tweet_ids.add(tweet.id)
                        posttime = tweet.created_at

                        if 'retweeted_status' in dir(tweet):
                           text=tweet.retweeted_status.full_text
                        else:
                           text=tweet.full_text

                        #text = re.sub(r'https:\/\/t.co\S{1,11}', '', text, flags=re.MULTILINE)
                        print(text)


                        c.writerow([str(tweet.id), str(posttime),text.replace("\n", " "), \
                                tweet.user.name, tweet.user.verified, tweet.user.followers_count,\
                                tweet.user.created_at])
                        f.flush()

                except tw.TweepError:
                    print("Error: too many requests")
                    time.sleep(300)
                time.sleep(10)
        f.close()
