from dataanalysis import DataAnalysis


s = DataAnalysis('Reading_TweetList.txt')
wordlist = ['RT','co','https','http','rdguk']

s.show_piechart()
s.print_sentiment_extremes()
s.show_hist()
s.show_worldcloud(wordlist)
s.FrequencyTimeGraph('Road')
