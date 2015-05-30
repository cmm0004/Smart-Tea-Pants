from django.test import TestCase
import mock
from tweetbot.models import User, TrainingData
from tweetbot.helpers.modelToArray import ModelDataToArray
from tweepy import API
from tweepy.models import User as TwitterUser, ResultSet, Status

import datetime
import numpy as np

def mock_get_data_array():
	return np.array([0,4,1,0,2,124,543,235,1,0,12,1,5432,1,0])

class ModelDataToArrayTestCase(TestCase):

	def setUp(self):
		User.objects.create(
			contributors_enabled = False,
			hours_since_last_tweet = 4,
			declared_blogger = True,
			declared_company = False,
			num_entities = 2,
			tweets_favorited = 124,
			num_followers = 543,
			num_friends = 235,
			geo_enabled = True,
			is_translator = False,
			listed_count = 12,
			protected = True,
			num_tweets = 5432,
			has_profile_url = True,
			verified = False,
			screen_name = 'Test',
			user_id = 1,
			classification = '?')
		
		TrainingData.objects.create(
			contributors_enabled = False,
			hours_since_last_tweet = None,
			declared_blogger = True,
			declared_company = False,
			num_entities = 2,
			tweets_favorited = 124,
			num_followers = 543,
			num_friends = 235,
			geo_enabled = True,
			is_translator = False,
			listed_count = 12,
			protected = True,
			num_tweets = 5432,
			has_profile_url = True,
			verified = False,
			classification = 'business')

	
	
	def test_get_data(self):

		model_to_array_obj = ModelDataToArray(User.objects.all())

		self.assertEqual(1, len(User.objects.all()))
		self.assertEqual(1, len(model_to_array_obj.get_data()))
		self.assertEqual(15, len(model_to_array_obj.get_data()[0]))
		
	def test_get_data_none_to_0(self):
		model_to_array_obj = ModelDataToArray(TrainingData.objects.all())

		self.assertEqual(1, len(TrainingData.objects.all()))
		self.assertEqual(1, len(model_to_array_obj.get_data()))
		self.assertEqual(15, len(model_to_array_obj.get_data()[0]))
		
		expected = np.int64()
		for value in model_to_array_obj.get_data()[0]:
			self.assertIsInstance(expected, type(value))
		
	def test_get_targets(self):
		model_to_array_obj = ModelDataToArray(TrainingData.objects.all())
		self.assertEqual(1, len(TrainingData.objects.all()))
		
		targets = model_to_array_obj.get_targets()

		self.assertEqual(1, len(targets))
		self.assertEqual('business', targets[0])




		