from django.db import models
from tweetbot.models import User

# Create your models here.

class Tweet(models.Model):
	"""model for Tweets as part of the 
		text processing module"""
 	#new_tweet[0].text
	text = models.CharField(max_length = 140)
	#new_tweet[0].id
	status_id = models.IntegerField(unique=True)
	#user object, pk is user_id
	#tweetbot.User.user_id
	user = models.ForeignKey(User)

class ParsedTweet(models.Model):

	"""model of the parsed tweet"""

	tweet = models.ForeignKey(Tweet)
	#positive or negitive -1 to 1
	polarity = models.DecimalField(max_digits=3, decimal_places=2)
	#opinion or fact 0 to 1, 1 is subjective
	subjectivity = models.DecimalField(max_digits=3, decimal_places=2)

