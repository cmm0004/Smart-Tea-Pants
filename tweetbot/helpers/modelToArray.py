import numpy as np

class ModelDataToArray(object):
	#array
	def __init__(self, model_data_query_set):
		self.model_data = model_data_query_set

	def get_data(self):
		rows  = []
		for model in self.model_data:
			data = [
			model.contributors_enabled,
			self._none_to_0(model.hours_since_last_tweet),
			model.declared_blogger,
			model.declared_company,
			model.num_entities,
			model.tweets_favorited,
			model.num_followers,
			model.num_friends,
			model.geo_enabled,
			model.is_translator,
			model.listed_count,
			model.protected,
			model.num_tweets,
			model.has_profile_url,
			model.verified
			]
			
			
			rows.append(data)

		return np.array(rows, dtype='int')

	def _none_to_0(self, data_point):
		if data_point == None:
			data_point = '0'
		return data_point

	def get_targets(self):
		targets = []
		for model in self.model_data:
			targets.append(model.classification)

		return np.array(targets)
