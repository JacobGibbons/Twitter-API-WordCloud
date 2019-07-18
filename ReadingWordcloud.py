from sentiment import Sentiment


s = Sentiment('Reading_TweetList.txt')
wordlist = ['RT','co','https','http','rdguk']
#s.show_piechart()

#s.show_worldcloud(wordlist)
s.FrequencyTimeGraph('Road')
