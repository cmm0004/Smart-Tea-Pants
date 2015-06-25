import os
import time
import tweepy
import datetime
import random
from tweetbot.helpers.auth import API
from tweetbot.helpers.follower import Follower
from tweetbot.helpers.search import Search
from tweetbot.helpers.personalize import WeekDayAware
from tweetbot.models import User, TrainingData
from hollaBack.models import Tweet, ParsedTweet
from django.db import IntegrityError
from textblob import TextBlob

class NLPHelper(object):
	def __init__(self, API):
		self.API = API

	def chooseUser(self):
		human_followers = User.objects.filter(classification='individual')
		if human_followers:
			return random.choice(human_followers)

	def saveRecentTweets(self, user, count=1):
		"""
			returns list of Tweet objects saved
		"""
		tweets = self.API.user_timeline(user_id=user.user_id, count=count)
		saved_tweets = []
		for status in tweets:
			new_tweet = Tweet(
				text=status.text,
				status_id=status.id,
				user=user
			)
			try:
				new_tweet.save()
				saved_tweets.append(new_tweet)
			except IntegrityError as e:
				print(e)
				continue
		return saved_tweets
			
	def parseTweet(self, Tweet):
		blob = TextBlob(Tweet.text)
		new_tweet = ParsedTweet(
				tweet=Tweet,
				polarity=blob.sentiment.polarity,
				subjectivity=blob.sentiment.subjectivity
			)
		try:
			new_tweet.save()
			return new_tweet	
		except IntegrityError as e:
			print(e)
		

	def getPositiveSubjective(self, count=1):
		tweets = ParsedTweet.objects.filter(subjectivity__gte=.5, polarity__gte=0)
		return tweets[0:count]

	def getNegativeSubjective(self, count=1):
		tweets = ParsedTweet.objects.filter(subjectivity__gte=.5, polarity__lte=0)
		return tweets[0:count]

	def getPositiveObjective(self, count=1):
		tweets = ParsedTweet.objects.filter(subjectivity__lte=.5, polarity__gte=0)
		return tweets[0:count]

	def getNegativeObjective(self, count=1):
		tweets = ParsedTweet.objects.filter(subjectivity__lte=.5, polarity__lte=0)
		return tweets[0:count]


	def _isSubjective(self, ParsedTweet):
		return True if ParsedTweet.subjectivity > 0.5 else False

	def _isPositive(self, ParsedTweet):
		return True if ParsedTweet.polarity > 0.0 else False



