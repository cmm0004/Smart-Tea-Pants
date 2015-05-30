import csv
from tweetbot.models import TrainingData

with open('tweetbot/TweetData2_Sheet1_training.csv') as file:
	reader = csv.reader(file)
	for row in reader:
		if row[1] == '':
			row[1] = None
		new_classified_user = TrainingData(
		contributors_enabled = row[0], #contributers_enabled
		hours_since_last_tweet = row[1], #hours_since_last_tweet
		declared_blogger = row[2], #declared_blogger
		declared_company = row[3], #declared_company
		num_entities = row[4], #num_entities
		tweets_favorited = row[5], #tweets_favorited
		num_followers = row[6], #num_followers
		num_friends = row[7], #num_friends
		geo_enabled = row[8], #geo_enabled
		is_translator = row[9], #is_translator
		listed_count = row[10], #listed_count
		protected = row[11], #protected
		num_tweets = row[12], #num_tweets
		has_profile_url = row[13], #has_profile_url
		verified = row[14],
		classification = row[15])
		
		new_classified_user.save()