from dataanalysis import DataAnalysis


s = DataAnalysis('VandB_TweetList.txt')
wordlist = (['RT','co','https','http','Baroda','Vadodara','SmartCitiesIndia'])

s.show_piechart()
s.print_sentiment_extremes()
s.show_hist()
s.show_worldcloud(wordlist)
s.FrequencyTimeGraph('Road')
