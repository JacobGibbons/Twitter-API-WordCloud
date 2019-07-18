from TweetSearch import TweetSearch



search_words = ['#Baroda','#Vadodara','#SmartCitiesIndia']
search_terms = ['Traffic','Transport','Mobility','Cycle','Congestion','Parking',
'\"Private Vehicles\"','Pollution','\"Multi Modal\"','E-Rickshaw','Roads','Bus',
'Flyover','\"Smart Cities\"','Bike','Car','Road','Walk','Footpath','Pedestrian',
'Rickshaw','Electric','Signal','Highway']

filename = 'VandB_TweetList.txt'

searcher = TweetSearch(filename,search_words,search_terms)
