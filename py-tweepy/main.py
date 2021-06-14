# via pip 
pip install tweepy

# via clone repo
git clone https://github.com/tweepy/tweepy.git
cd tweepy
pip install

# install dari github
pip install git+https://github.com/tweepy/tweepy.git

import tweepy
import csv
access_token=""
access_token_secret=""
consumer_key=""
consumer_key_secret=""
auth = tweepy.OAuthHandler(consumer_key,consumer_key_secret)
api = tweepy.API(auth)
# Open/create a file to append data to
csvFile = open('nama-file.csv', 'w', encoding='utf-8')
#Use csv writer
csvWriter = csv.writer(csvFile)
for tweet in tweepy.Cursor(api.search, q='#Python -filter:retweets', tweet_mode='extended',lang="id", since='2021-01-01', until='2021-01-10').items(100):
    text = tweet.full_text
    user = tweet.user.name
    created = tweet.created_at
    csvWriter.writerow([created, text.encode('utf-8'), user])
csvWriter = csv.writer(csvFile)
csvFile.close()

# upgrade student premium membership
# https://developer.twitter.com/en/products/twitter-api/academic-research
