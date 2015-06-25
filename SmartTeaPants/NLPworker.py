import os
import time
import tweepy
import datetime
from tweetbot.helpers.auth import API
from tweetbot.helpers.follower import Follower
from hollaBack import NLPhelper

def main():
	if 'HEROKU_CONSUMER_KEY' in os.environ:
		CONSUMER_KEY = os.environ['HEROKU_CONSUMER_KEY']
		CONSUMER_SECRET = os.environ['HEROKU_CONSUMER_SECRET']
		ACCESS_TOKEN = os.environ['HEROKU_ACCESS_TOKEN']
		ACCESS_SECRET = os.environ['HEROKU_ACCESS_SECRET']

		twitter_api = API(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET, access_token=ACCESS_TOKEN, access_token_secret=ACCESS_SECRET)
	else:
		twitter_api = API()
	
	TWITTER_BOT = twitter_api.authenticate()

	saved_tweets = None
	user = None
	parsed_tweets = None

	followers = Follower(TWITTER_BOT)

	NLP_helper = NLPhelper.NLPHelper(TWITTER_BOT)
	try:
		user = NLP_helper.chooseUser()
	except tweepy.TweepError as e:
		print(e)
	if user:
		saved_tweets = NLP_helper.saveRecentTweets(user, 5)
	if saved_tweets:
		parsed_tweets = []
		for tweet in saved_tweets:
			#this saves each in parse tweet table.
			saved_tweet = NLP_helper.parseTweet(tweet)
			parsed_tweets.append(saved_tweet)
	if parsed_tweets:		
		for tweet in parsed_tweets:
			print(tweet.tweet.text)
	else:
		print('no new parsed tweets')
	
main()

			


