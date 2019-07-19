# Twitter Wordcloud

This project consists of multiple programs. The first is necessary in order to use the others, it continuously searches Twitter for tweets based on search terms provided and stores the found tweets in a csv format file. Search terms can be hashtags or specific words, the example files are called 'Reading_TweetList.txt' and 'VandB_TweetList.txt'. The other programs then display this information in a multitude of ways:

Wordclouds

Frequency Time Graphs

Sentiment Pie Charts and Histograms

### Prerequisites

This program depends on the packages listed in 'requirements.txt', these packages can be installed via pip using the following command.
With the following packages installed, you will be able to use the program.
```
pip3 install -r requirements.txt
```
### Installing

In order to run the Twitter search program; a Twitter API key and secret key must be provided; the name of the file the tweets are stored in (whether it exists or not) must be provided; 'search_words' or 'search_terms' must consist of at least one word or term.

The rest of the programs requirements can be found in 'dataanalysis.py'.
