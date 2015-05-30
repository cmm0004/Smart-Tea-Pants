from tweetbot.helpers.APIKeys import APIKeys
import tweepy
import sys


class API(object):
	def __init__(self, consumer_key=None, consumer_secret=None, access_token=None, access_token_secret=None):
		if consumer_key == None:
			api_keys = APIKeys()
			self.consumer_key = api_keys.consumer_key
			self.consumer_secret = api_keys.consumer_secret
			self.access_token = api_keys.access_token
			self.access_token_secret = api_keys.access_token_secret
			self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
			self.auth.secure = True
			self.auth.set_access_token(self.access_token, self.access_token_secret)
		else:
			self.consumer_key = api_keys.consumer_key
			self.consumer_secret = api_keys.consumer_secret
			self.access_token = api_keys.access_token
			self.access_token_secret = api_keys.access_token_secret
			self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
			self.auth.secure = True
			self.auth.set_access_token(self.access_token, self.access_token_secret)

	def authenticate(self):
		return tweepy.API(self.auth)