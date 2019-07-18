from sentiment import Sentiment


s = Sentiment('VandB_TweetList.txt')

wordlist = (['RT','co','https','http','Baroda','Vadodara','SmartCitiesIndia'])
s.show_piechart()
s.show_worldcloud(wordlist)
