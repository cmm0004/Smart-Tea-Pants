
import re
import tweepy
import time
from tweetbot.helpers.auth import API
from datetime import datetime
from tweetbot.models import User

	
def parseDescriptionBlogger(userDescription):
	needle = re.compile('blog|blogger|blogging')
	match = re.search(needle, userDescription.lower())
	return not not match	

def parseDescriptionCompany(userDescription):
	needle = re.compile('hand.crafted|store|sell|selling|business|company|buy|sale|discount|artisan|hand.made|tea.blends|start.up')
	match = re.search(needle, userDescription.lower())
	return not not match

def getHourDeltaRecentTweet(userobject):
	if not userobject.protected:
		try:
			recent_tweet_results = BOT.user_timeline(user_id=userobject.id, count=1)
		except:
			print('twitter api is sleepy, waiting 3 mins')
			time.sleep(60)
			print('2 minutes')
			time.sleep(60)
			print('1 minute')
			time.sleep(60)
			print('resuming')
			return 'retry'
		if len(recent_tweet_results) > 0:
			tweet_made = recent_tweet_results[0].created_at
			now = datetime.now()
			delta = now - tweet_made
			seconds = delta.total_seconds()
			if seconds <= 3600:
				return '0'
			return seconds//3600
	return '?'
failures = []
def saveRowsofFollowerData(all_ids):
	row = []
	
	for userid in all_ids:	
		try:	
			user_obj = BOT.get_user(id=userid)
		except:
			print('twitter api is sleepy, waiting 3 mins')
			time.sleep(60)
			print('2 minutes')
			time.sleep(60)
			print('1 minute')
			time.sleep(60)
			print('resuming')
			failures.append(userid)
			continue
		if user_obj.lang == 'en':
			
			hourdelta = getHourDeltaRecentTweet(user_obj)
			if hourdelta == 'retry':
				failures.append(userid)
				continue

		
			#assemble the data
			row = User(contributors_enabled = not not user_obj.contributors_enabled, #contributers_enabled
			hours_since_last_tweet = hourdelta, #hours_since_last_tweet
			declared_blogger = parseDescriptionBlogger(user_obj.description), #declared_blogger
			declared_company = parseDescriptionCompany(user_obj.description), #declared_company
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
			row.save()
		
			
api = API()
BOT = api.authenticate()

ids = BOT.followers_ids(screen_name='TeasontheLoose');

saveRowsofFollowerData([ids[0]])