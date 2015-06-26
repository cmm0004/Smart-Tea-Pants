from django.db import models
from tweetbot.models import User
# Create your models here.


class TrainingData(models.Model):
	"""
	TrainingData is a classified User
	"""
	user = models.ForeignKey(User, unique=True)
	classification = models.CharField(max_length=50)
