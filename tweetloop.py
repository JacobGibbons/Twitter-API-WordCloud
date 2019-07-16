from wordcloud import WordCloud, STOPWORDS
import tweepy as tw
import matplotlib.pyplot as plot
import json

Tweets_dict = dict()
file = "TweetList.txt"
Key = 'wjQqcP8hTwOUBHBca7Ens3cZH'
Secret = 'c6ZNbGfoo4cW0Sy0MgoerWMeaKa9wdH7O1zjljx4MKN6i3onvu'
auth = tw.OAuthHandler(Key, Secret)
api = tw.API(auth)
search_words = ['#rdguk','#Reading2050']
terms_grouped = []
#while True:
with open(file,"r") as f:
    Tweets_dict = json.load(f)

search_terms = ('Traffic','Transport','Mobility','Bicycle','Congestion',
'Parking','\"Private Vehicles\"','\"Rapid Transit\"','Pollution','\"Multi Modal\"',
'Roads','\"Electric Vehicles\"','Bus','\"Smart Cities\"','Car','Road','Walk',
'Pavement','Pedestrian','Electric','\"Traffic lights\"','Motorway')
for i in range(0,len(search_terms),4):
    group = search_terms[i:i+4]
    query_string = " OR ".join(search_words)+" "+" OR ".join(group)
    tweets = tw.Cursor(api.search, q=query_string, lang='en').items(25)
    for tweet in tweets:
        Tweets_dict[tweet.id] = tweet.text

with open(file,"w") as f:
    f.write(json.dumps(Tweets_dict))
