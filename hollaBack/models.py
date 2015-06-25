from django.db import models
from tweetbot.models import User

# Create your models here.

class Tweet(models.Model):
	"""model for Tweets as part of the 
		text processing module"""

	text = models.CharField(max_length = 140)
	status_id = models.IntegerField()
	user = models.ForeignKey(User)

class ParsedTweet(models.Model):

	"""model of the parsed tweet"""

	tweet = models.ForeignKey(Tweet)
	#positive or negitive -1 to 1
	polarity = models.FloatField()
	#opinion or fact 0 to 1, 1 is subjective
	subjectivity = models.FloatField()

