from django.db import models
from tweetbot.helpers.modelToArray import ModelDataToArray
from datetime import datetime
import time, re
from django.db import IntegrityError
from django.db.models import F

#most recent addition will be user.objects.first()
class User(models.Model):
	contributors_enabled = models.BooleanField()
	hours_since_last_tweet = models.IntegerField(null=True)
	declared_blogger = models.BooleanField()
	declared_company = models.BooleanField()
	num_entities = models.IntegerField()
	tweets_favorited = models.IntegerField()
	num_followers = models.IntegerField()
	num_friends = models.IntegerField()
	geo_enabled = models.BooleanField()
	is_translator = models.BooleanField()
	listed_count = models.IntegerField()
	protected = models.BooleanField()
	num_tweets = models.IntegerField()
	has_profile_url = models.BooleanField()
	verified = models.BooleanField()
	screen_name = models.CharField(max_length = 50)
	user_id = models.IntegerField(primary_key = True)
	classification = models.CharField(default='?', max_length=50)

	def __str__(self):
		return self.screen_name


	def update_classification(self, pk, new_classification):
		updated_user = self.objects.get(user_id=pk)
		updated_user.classification = new_classification
		updated_user.save()

	def saveFromFollowers(self, TWEET_BOT, userid):
		
		user_obj = TWEET_BOT.get_user(id=userid)
		
		if user_obj.lang == 'en':
			hourdelta = self._getHourDeltaRecentTweet(BOT=TWEET_BOT, userobject=user_obj)
			
			row = User(contributors_enabled = not not user_obj.contributors_enabled, #contributers_enabled
					hours_since_last_tweet = hourdelta, #hours_since_last_tweet
					declared_blogger = self._parseDescriptionBlogger(userDescription=user_obj.description), #declared_blogger
					declared_company = self._parseDescriptionCompany(userDescription=user_obj.description), #declared_company
					num_entities = len(user_obj.entities), #num_entities
					tweets_favorited = user_obj.favourites_count, #tweets_favorited
					num_followers = user_obj.followers_count, #num_followers
					num_friends = user_obj.friends_count, #num_friends
					geo_enabled = not not user_obj.geo_enabled, #geo_enabled
					is_translator = not not user_obj.is_translator, #is_translator
					listed_count = user_obj.listed_count, #listed_count
					protected = not not user_obj.protected, #protected
					num_tweets = user_obj.statuses_count, #num_tweets
					has_profile_url = not not user_obj.url, #has_profile_url
					verified = not not user_obj.verified, #verified
					screen_name = user_obj.screen_name, #screen_name, for my usage
					user_id = user_obj.id) #id, for debugging
			try:
				print(row)
				row.save()
				return True
			except IntegrityError as e:
				print(e)
				return False

	def _parseDescriptionBlogger(self, userDescription):
		needle = re.compile('blog|blogger|blogging')
		match = re.search(needle, userDescription.lower())
		return not not match	

	def _parseDescriptionCompany(self, userDescription):
		needle = re.compile('hand.crafted|store|sell|selling|order|business|company|buy|sale|discount|artisan|hand.made|tea.blends|start.up')
		match = re.search(needle, userDescription.lower())
		return not not match

	def _getHourDeltaRecentTweet(self, BOT, userobject):
		if not userobject.protected:
			recent_tweet_results = BOT.user_timeline(user_id=userobject.id, count=1)
			if len(recent_tweet_results) > 0:
				tweet_made = recent_tweet_results[0].created_at
				now = datetime.now()
				delta = now - tweet_made
				seconds = delta.total_seconds()
				if seconds <= 3600:
					return '0'
				return seconds//3600
		return None

	##need a userDataToArray now.
	def get_data(self, user_data_query):
		array_maker = ModelDataToArray(user_data_query)
		return array_maker.get_data()

class TrainingData(models.Model):
	contributors_enabled = models.BooleanField()
	hours_since_last_tweet = models.IntegerField(null=True)
	declared_blogger = models.BooleanField()
	declared_company = models.BooleanField()
	num_entities = models.IntegerField()
	tweets_favorited = models.IntegerField()
	num_followers = models.IntegerField()
	num_friends = models.IntegerField()
	geo_enabled = models.BooleanField()
	is_translator = models.BooleanField()
	listed_count = models.IntegerField()
	protected = models.BooleanField()
	num_tweets = models.IntegerField()
	has_profile_url = models.BooleanField()
	verified = models.BooleanField()
	classification = models.CharField(default='?', max_length=50)


	def get_targets(self):
		td = self.objects.all()
		array_maker = ModelDataToArray(td)
		return array_maker.get_targets()
##got the targets, next time get the data
	def get_data(self):
		td = self.objects.all()
		array_maker = ModelDataToArray(td)

		return array_maker.get_data()

	def save_from_users(self, user_object_queryset, classification):
		
		for user in user_object_queryset:
			if (user.declared_blogger):
				classification = 'blogger'
			elif (user.declared_company):
				classification = 'business'
				
			row = TrainingData(
				contributors_enabled=user.contributors_enabled,
				hours_since_last_tweet=user.hours_since_last_tweet,
				declared_blogger=user.declared_blogger,
				declared_company=user.declared_company,
				num_entities=user.num_entities,
				tweets_favorited=user.tweets_favorited,
				num_followers=user.num_followers,
				num_friends=user.num_friends,
				geo_enabled=user.geo_enabled,
				is_translator=user.is_translator,
				listed_count=user.listed_count,
				protected=user.protected,
				num_tweets=user.num_tweets,
				has_profile_url=user.has_profile_url,
				verified=user.verified,
				classification=classification)
			if self._is_dupe(self, user=user, classification=classification):
				print(user.screen_name + ' is a dupe, not saving to TD')
				return
			try:
				row.save()
			except IntegrityError as e:
				print(e)
	
	def _is_dupe(self, user, classification):
		dupes = self.objects.filter(contributors_enabled=user.contributors_enabled
			).filter(declared_blogger=user.declared_blogger
			).filter(declared_company=user.declared_company
			).filter(num_entities=user.num_entities
			).filter(tweets_favorited=user.tweets_favorited
			).filter(num_followers=user.num_followers
			).filter(num_friends=user.num_friends
			).filter(geo_enabled=user.geo_enabled
			).filter(is_translator=user.is_translator
			).filter(listed_count=user.listed_count
			).filter(protected=user.protected
			).filter(num_tweets=user.num_tweets
			).filter(has_profile_url=user.has_profile_url
			).filter(verified=user.verified
			).filter(classification=user.classification
			)
		if len(dupes) > 0:
			return True
		return False

class Tea(models.Model):
	name = models.CharField(max_length=200)
	month_int = models.IntegerField()
	tea_type = models.CharField(max_length=200)
		
	def __str__(self):
		return self.name

	def get_teas_available(self, month):
		return self.objects.filter(month_int=month)


# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')


# class Choice(models.Model):
#     question = models.ForeignKey(Question)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
