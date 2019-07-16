from wordcloud import WordCloud, STOPWORDS
import tweepy as tw
import matplotlib.pyplot as plot


Key = 'wjQqcP8hTwOUBHBca7Ens3cZH'
Secret = 'c6ZNbGfoo4cW0Sy0MgoerWMeaKa9wdH7O1zjljx4MKN6i3onvu'

auth = tw.OAuthHandler(Key, Secret)
api = tw.API(auth)
#search_words = '#rdguk OR #Reading2050'
search_words = ['#rdguk','#Reading2050']
tweets = tw.Cursor(api.search, q=" OR ".join(search_words), lang='en').items(25)
TweetsList = [tweet.text for tweet in tweets]
#print(TweetsList)
for i in TweetsList:
    if '#Reading2050' in i:
        print('test')
for idx,tweet in enumerate(TweetsList):
    if 'https' in tweet:
        TweetsList[idx]= tweet[:tweet.index('https')]
wc = WordCloud(stopwords = STOPWORDS)
wc.generate(" ".join(TweetsList))
plot.imshow(wc)
plot.show()
#print(TweetsList)
