from TweetSearch import TweetSearch


search_words = ['#rdguk','#Reading2050']
search_terms = ['Traffic','Transport','Mobility','Bicycle','Congestion',
'Parking','\"Private Vehicles\"','\"Rapid Transit\"','Pollution','\"Multi Modal\"',
'Roads','\"Electric Vehicles\"','Bus','\"Smart Cities\"','Car','Road','Walk',
'Pavement','Pedestrian','Electric','\"Traffic lights\"','Motorway']

filename = 'Reading_TweetList.txt'

searcher = TweetSearch(filename,search_words,search_terms)
