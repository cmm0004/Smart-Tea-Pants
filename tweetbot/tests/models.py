from django.test import TestCase
import mock
from tweetbot.models import User, TrainingData
from tweetbot.helpers.modelToArray import ModelDataToArray
from tweepy import API
from tweepy.models import User as TwitterUser, ResultSet, Status

import datetime

# Create your tests here.

def mock_get_user(id=None):
	mock_twitteruser = TwitterUser()

	
	mock_twitteruser.contributors_enabled=1
	mock_twitteruser.description='blogger'
	mock_twitteruser.entities=[1,2,3]
	mock_twitteruser.favourites_count=1
	mock_twitteruser.followers_count=1
	mock_twitteruser.friends_count=1
	mock_twitteruser.geo_enabled=False
	mock_twitteruser.is_translator=False
	mock_twitteruser.listed_count=1
	mock_twitteruser.protected=False
	mock_twitteruser.statuses_count=1
	mock_twitteruser.url=''
	mock_twitteruser.verified=False
	mock_twitteruser.screen_name='Test2'
	mock_twitteruser.id=2
	mock_twitteruser.lang='en'

	return mock_twitteruser

def mock_get_user_protected(id=None):
	mock_twitteruser = TwitterUser()

	
	mock_twitteruser.contributors_enabled=1
	mock_twitteruser.description='blogger'
	mock_twitteruser.entities=[1,2,3]
	mock_twitteruser.favourites_count=1
	mock_twitteruser.followers_count=1
	mock_twitteruser.friends_count=1
	mock_twitteruser.geo_enabled=False
	mock_twitteruser.is_translator=False
	mock_twitteruser.listed_count=1
	mock_twitteruser.protected=True
	mock_twitteruser.statuses_count=1
	mock_twitteruser.url=''
	mock_twitteruser.verified=False
	mock_twitteruser.screen_name='Test2'
	mock_twitteruser.id=2
	mock_twitteruser.lang='en'

	return mock_twitteruser

#last tweet 4 hours previous
def mock_user_timeline(user_id=None, count=None):
	status = Status()

	now = datetime.datetime.now()
	hours_since = now - datetime.timedelta(hours=4)

	status.created_at = hours_since
	return [status]
	#[Status(
	#	in_reply_to_screen_name='annemariayritys', created_at=datetime.datetime(2015, 5, 6, 7, 44, 46), source='TeaTweetBot', source_url='https://github.com/cmm0004/TeaTweetBot', in_reply_to_user_id=330509973, id_str='595856716585160705', in_reply_to_status_id_str=None, entities={'urls': [], 'user_mentions': [{'id_str': '330509973', 'screen_name': 'annemariayritys', 'indices': [0, 16], 'id': 330509973, 'name': 'Anne-Maria Yritys'}], 'symbols': [], 'hashtags': [{'indices': [63, 78], 'text': 'teasontheloose'}]}, author=TwitterUser(listed_count=15, location='Atlanta', profile_use_background_image=True, description='An Atlanta-based start-up to help you discover new and interesting teas, join us at http://t.co/jRB3QT9I6k and follow along on our tea adventure!', entities={'url': {'urls': [{'url': 'http://t.co/Re7vNaFeuh', 'indices': [0, 22], 'expanded_url': 'http://www.teasontheloose.com', 'display_url': 'teasontheloose.com'}]}, 'description': {'urls': [{'url': 'http://t.co/jRB3QT9I6k', 'indices': [84, 106], 'expanded_url': 'http://teasontheloose.com', 'display_url': 'teasontheloose.com'}]}}, time_zone=None, protected=False, default_profile_image=False, geo_enabled=False, followers_count=735, profile_background_image_url='http://pbs.twimg.com/profile_background_images/378800000182258644/mX13UXQR.png', default_profile=False, profile_image_url='http://pbs.twimg.com/profile_images/378800000699341883/63ad52263e1c0531982e212aff01e367_normal.jpeg', url='http://t.co/Re7vNaFeuh', profile_image_url_https='https://pbs.twimg.com/profile_images/378800000699341883/63ad52263e1c0531982e212aff01e367_normal.jpeg', favourites_count=788, following=False, _json={'profile_use_background_image': True, 'listed_count': 15, 'id_str': '2176595588', 'notifications': False, 'profile_background_image_url_https': 'https://pbs.twimg.com/profile_background_images/378800000182258644/mX13UXQR.png', 'profile_sidebar_fill_color': 'DDEEF6', 'profile_background_tile': False, 'location': 'Atlanta', 'description': 'An Atlanta-based start-up to help you discover new and interesting teas, join us at http://t.co/jRB3QT9I6k and follow along on our tea adventure!', 'entities': {'url': {'urls': [{'url': 'http://t.co/Re7vNaFeuh', 'indices': [0, 22], 'expanded_url': 'http://www.teasontheloose.com', 'display_url': 'teasontheloose.com'}]}, 'description': {'urls': [{'url': 'http://t.co/jRB3QT9I6k', 'indices': [84, 106], 'expanded_url': 'http://teasontheloose.com', 'display_url': 'teasontheloose.com'}]}}, 'default_profile_image': False, 'time_zone': None, 'followers_count': 735, 'protected': False, 'created_at': 'Tue Nov 05 18:38:26 +0000 2013', 'verified': False, 'is_translation_enabled': False, 'profile_sidebar_border_color': 'FFFFFF', 'geo_enabled': False, 'favourites_count': 788, 'screen_name': 'TeasontheLoose', 'profile_background_image_url': 'http://pbs.twimg.com/profile_background_images/378800000182258644/mX13UXQR.png', 'default_profile': False, 'profile_link_color': '0084B4', 'profile_image_url': 'http://pbs.twimg.com/profile_images/378800000699341883/63ad52263e1c0531982e212aff01e367_normal.jpeg', 'url': 'http://t.co/Re7vNaFeuh', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/378800000699341883/63ad52263e1c0531982e212aff01e367_normal.jpeg', 'follow_request_sent': False, 'profile_text_color': '333333', 'lang': 'en', 'friends_count': 1111, 'following': False, 'is_translator': False, 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/2176595588/1391634450', 'utc_offset': None, 'name': 'Teas on the Loose', 'contributors_enabled': False, 'profile_background_color': 'CCBC9F', 'statuses_count': 689, 'id': 2176595588}, profile_background_color='CCBC9F', _api=<tweepy.api.API object at 0x10da6a400>, utc_offset=None, follow_request_sent=False, profile_sidebar_fill_color='DDEEF6', profile_background_image_url_https='https://pbs.twimg.com/profile_background_images/378800000182258644/mX13UXQR.png', name='Teas on the Loose', verified=False, screen_name='TeasontheLoose', profile_banner_url='https://pbs.twimg.com/profile_banners/2176595588/1391634450', notifications=False, profile_sidebar_border_color='FFFFFF', is_translation_enabled=False, profile_link_color='0084B4', id_str='2176595588', profile_text_color='333333', created_at=datetime.datetime(2013, 11, 5, 18, 38, 26), lang='en', friends_count=1111, is_translator=False, profile_background_tile=False, contributors_enabled=False, statuses_count=689, id=2176595588), favorite_count=0, id=595856716585160705, place=None, in_reply_to_status_id=None, coordinates=None, in_reply_to_user_id_str='330509973', user=TwitterUser(listed_count=15, location='Atlanta', profile_use_background_image=True, description='An Atlanta-based start-up to help you discover new and interesting teas, join us at http://t.co/jRB3QT9I6k and follow along on our tea adventure!', entities={'url': {'urls': [{'url': 'http://t.co/Re7vNaFeuh', 'indices': [0, 22], 'expanded_url': 'http://www.teasontheloose.com', 'display_url': 'teasontheloose.com'}]}, 'description': {'urls': [{'url': 'http://t.co/jRB3QT9I6k', 'indices': [84, 106], 'expanded_url': 'http://teasontheloose.com', 'display_url': 'teasontheloose.com'}]}}, time_zone=None, protected=False, default_profile_image=False, geo_enabled=False, followers_count=735, profile_background_image_url='http://pbs.twimg.com/profile_background_images/378800000182258644/mX13UXQR.png', default_profile=False, profile_image_url='http://pbs.twimg.com/profile_images/378800000699341883/63ad52263e1c0531982e212aff01e367_normal.jpeg', url='http://t.co/Re7vNaFeuh', profile_image_url_https='https://pbs.twimg.com/profile_images/378800000699341883/63ad52263e1c0531982e212aff01e367_normal.jpeg', favourites_count=788, following=False, _json={'profile_use_background_image': True, 'listed_count': 15, 'id_str': '2176595588', 'notifications': False, 'profile_background_image_url_https': 'https://pbs.twimg.com/profile_background_images/378800000182258644/mX13UXQR.png', 'profile_sidebar_fill_color': 'DDEEF6', 'profile_background_tile': False, 'location': 'Atlanta', 'description': 'An Atlanta-based start-up to help you discover new and interesting teas, join us at http://t.co/jRB3QT9I6k and follow along on our tea adventure!', 'entities': {'url': {'urls': [{'url': 'http://t.co/Re7vNaFeuh', 'indices': [0, 22], 'expanded_url': 'http://www.teasontheloose.com', 'display_url': 'teasontheloose.com'}]}, 'description': {'urls': [{'url': 'http://t.co/jRB3QT9I6k', 'indices': [84, 106], 'expanded_url': 'http://teasontheloose.com', 'display_url': 'teasontheloose.com'}]}}, 'default_profile_image': False, 'time_zone': None, 'followers_count': 735, 'protected': False, 'created_at': 'Tue Nov 05 18:38:26 +0000 2013', 'verified': False, 'is_translation_enabled': False, 'profile_sidebar_border_color': 'FFFFFF', 'geo_enabled': False, 'favourites_count': 788, 'screen_name': 'TeasontheLoose', 'profile_background_image_url': 'http://pbs.twimg.com/profile_background_images/378800000182258644/mX13UXQR.png', 'default_profile': False, 'profile_link_color': '0084B4', 'profile_image_url': 'http://pbs.twimg.com/profile_images/378800000699341883/63ad52263e1c0531982e212aff01e367_normal.jpeg', 'url': 'http://t.co/Re7vNaFeuh', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/378800000699341883/63ad52263e1c0531982e212aff01e367_normal.jpeg', 'follow_request_sent': False, 'profile_text_color': '333333', 'lang': 'en', 'friends_count': 1111, 'following': False, 'is_translator': False, 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/2176595588/1391634450', 'utc_offset': None, 'name': 'Teas on the Loose', 'contributors_enabled': False, 'profile_background_color': 'CCBC9F', 'statuses_count': 689, 'id': 2176595588}, profile_background_color='CCBC9F', _api=<tweepy.api.API object at 0x10da6a400>, utc_offset=None, follow_request_sent=False, profile_sidebar_fill_color='DDEEF6', profile_background_image_url_https='https://pbs.twimg.com/profile_background_images/378800000182258644/mX13UXQR.png', name='Teas on the Loose', verified=False, screen_name='TeasontheLoose', profile_banner_url='https://pbs.twimg.com/profile_banners/2176595588/1391634450', notifications=False, profile_sidebar_border_color='FFFFFF', is_translation_enabled=False, profile_link_color='0084B4', id_str='2176595588', profile_text_color='333333', created_at=datetime.datetime(2013, 11, 5, 18, 38, 26), lang='en', friends_count=1111, is_translator=False, profile_background_tile=False, contributors_enabled=False, statuses_count=689, id=2176595588), retweet_count=0, geo=None, lang='en', contributors=None, favorited=True, retweeted=False, _json={'in_reply_to_screen_name': 'annemariayritys', 'created_at': 'Wed May 06 07:44:46 +0000 2015', 'source': '<a href="https://github.com/cmm0004/TeaTweetBot" rel="nofollow">TeaTweetBot</a>', 'retweeted': False, 'in_reply_to_user_id': 330509973, 'retweet_count': 0, 'in_reply_to_status_id_str': None, 'entities': {'urls': [], 'user_mentions': [{'id_str': '330509973', 'screen_name': 'annemariayritys', 'indices': [0, 16], 'id': 330509973, 'name': 'Anne-Maria Yritys'}], 'symbols': [], 'hashtags': [{'indices': [63, 78], 'text': 'teasontheloose'}]}, 'favorite_count': 0, 'id': 595856716585160705, 'place': None, 'in_reply_to_status_id': None, 'coordinates': None, 'in_reply_to_user_id_str': '330509973', 'user': {'profile_use_background_image': True, 'listed_count': 15, 'id_str': '2176595588', 'notifications': False, 'profile_background_image_url_https': 'https://pbs.twimg.com/profile_background_images/378800000182258644/mX13UXQR.png', 'profile_sidebar_fill_color': 'DDEEF6', 'profile_background_tile': False, 'location': 'Atlanta', 'description': 'An Atlanta-based start-up to help you discover new and interesting teas, join us at http://t.co/jRB3QT9I6k and follow along on our tea adventure!', 'entities': {'url': {'urls': [{'url': 'http://t.co/Re7vNaFeuh', 'indices': [0, 22], 'expanded_url': 'http://www.teasontheloose.com', 'display_url': 'teasontheloose.com'}]}, 'description': {'urls': [{'url': 'http://t.co/jRB3QT9I6k', 'indices': [84, 106], 'expanded_url': 'http://teasontheloose.com', 'display_url': 'teasontheloose.com'}]}}, 'default_profile_image': False, 'time_zone': None, 'followers_count': 735, 'protected': False, 'created_at': 'Tue Nov 05 18:38:26 +0000 2013', 'verified': False, 'is_translation_enabled': False, 'profile_sidebar_border_color': 'FFFFFF', 'geo_enabled': False, 'favourites_count': 788, 'screen_name': 'TeasontheLoose', 'profile_background_image_url': 'http://pbs.twimg.com/profile_background_images/378800000182258644/mX13UXQR.png', 'default_profile': False, 'profile_link_color': '0084B4', 'profile_image_url': 'http://pbs.twimg.com/profile_images/378800000699341883/63ad52263e1c0531982e212aff01e367_normal.jpeg', 'url': 'http://t.co/Re7vNaFeuh', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/378800000699341883/63ad52263e1c0531982e212aff01e367_normal.jpeg', 'follow_request_sent': False, 'profile_text_color': '333333', 'lang': 'en', 'friends_count': 1111, 'following': False, 'is_translator': False, 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/2176595588/1391634450', 'utc_offset': None, 'name': 'Teas on the Loose', 'contributors_enabled': False, 'profile_background_color': 'CCBC9F', 'statuses_count': 689, 'id': 2176595588}, 'id_str': '595856716585160705', 'geo': None, 'lang': 'en', 'contributors': None, 'favorited': True, 'text': '@annemariayritys Thank you for the follow! Happy tea drinking! #teasontheloose', 'truncated': False}, text='@annemariayritys Thank you for the follow! Happy tea drinking! #teasontheloose', _api=<tweepy.api.API object at 0x10da6a400>, truncated=False)])

#last tweet less than an hour previous
def mock_user_timeline_more_active(user_id=None, count=None):
	status = Status()

	now = datetime.datetime.now()
	hours_since = now - datetime.timedelta(minutes=30)

	status.created_at = hours_since
	return [status]

class UserTestCase(TestCase):
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
		now = datetime.datetime.now()
		self.hours_since = now - datetime.timedelta(hours=4)
		

	@mock.patch("tweepy.API.get_user", mock_get_user)
	@mock.patch("tweepy.API.user_timeline", mock_user_timeline)
	def test_save_from_followers(self):
		u = User()
		before_count = len(User.objects.all())

		u.saveFromFollowers(API, 1)
		self.assertEqual((before_count + 1), len(User.objects.all()))

		twitter_added_user = User.objects.filter(user_id=2)

		self.assertEqual(1, len(twitter_added_user))
		self.assertEqual(4, twitter_added_user[0].hours_since_last_tweet)
		self.assertTrue(twitter_added_user[0].declared_blogger)
		self.assertFalse(twitter_added_user[0].declared_company)

	@mock.patch("tweepy.API.user_timeline", mock_user_timeline)
	def test__getHourDeltaRecentTweet(self):
		u = User()
		userobject = mock_get_user()
		hourDelta = u._getHourDeltaRecentTweet(API, userobject)
		self.assertEqual(4, hourDelta)

	@mock.patch("tweepy.API.user_timeline", mock_user_timeline_more_active)
	def test__getHourDeltaRecentTweet_active(self):
		u = User()
		userobject = mock_get_user()
		hourDelta = u._getHourDeltaRecentTweet(API, userobject)

		self.assertEqual('0', hourDelta)
	
	@mock.patch("tweepy.API.user_timeline", mock_user_timeline)
	def test__getHourDeltaRecentTweet_protected_user(self):
		u = User()
		userobject = mock_get_user_protected()
		hourDelta = u._getHourDeltaRecentTweet(API, userobject)

		self.assertIsNone(hourDelta)

class TrainingDataTestCase(TestCase):
	
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

	def test_save_from_users(self):
		td = TrainingData()
		self.assertEqual(0, len(TrainingData.objects.all()))
		user_object_queryset = User.objects.all()
		self.assertEqual(1, len(user_object_queryset))
		
		td.save_from_users(user_object_queryset, 'business')
		self.assertEqual(1, len(TrainingData.objects.all()))



