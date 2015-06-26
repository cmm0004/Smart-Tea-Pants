from loveAngelMusicOrBaby.models import TrainingData
import numpy
import re
from sklearn import tree

class ClassifierHelper(object):
	"""
	params: NumpyHelper object, optional classifier defaults to 
	sklearn.tree.DecisionTreeClassifier
	"""
	def __init__(self, numpy_helper, classifier=tree.DecisionTreeClassifier()):
		self.numpy_helper = numpy_helper
		self.classifier = classifier
		
	def fit_classifier(self):
		"""
		fits a classifier with training data
		return: fitted Classifier object
		"""
        target = numpy_helper.get_targets()
        data = numpy_helper.get_data()

        return classifier.fit(data, target)

class UserHelper(object):
	""" 
	helper class to translate users to new training data rows
	
	"""

	def __init__(self):
		 
	def save_user_as_TrainingData(self, user, classification):
	""" 
	helper class to translate classified users to new training data rows
	params: user object, classification
	return: new training data
	"""
		
		if (user.declared_blogger):
			classification = 'blogger'
		elif (user.declared_company):
			classification = 'business'
			
		row = TrainingData(
			user=user
			classification=classification
		)

		try:
			row.save()
			return row 
		except IntegrityError as e:
			print(e)
	
class NumpyHelper(object):
	""" helper class for convert the model to numpy array """

	def __init__(self, querySet):
		self.querySet = querySet

	def get_data(self):
		""" param: querySet of models
			return: numpy array of arrays of data for the classifier to read
		"""
		rows  = []
				for model in self.querySet:
					data = [
						model.user.contributors_enabled,
						self._none_to_0(model.user.hours_since_last_tweet),
						model.user.declared_blogger,
						model.user.declared_company,
						model.user.num_entities,
						model.user.tweets_favorited,
						model.user.num_followers,
						model.user.num_friends,
						model.user.geo_enabled,
						model.user.is_translator,
						model.user.listed_count,
						model.user.protected,
						model.user.num_tweets,
						model.user.has_profile_url,
						model.user.verified
					]
					
					
					rows.append(data)

			return numpy.array(rows, dtype='int')

	def get_targets(self):
		"""
		return: numpy array of the targets for self.querySet
		"""
		targets = []
		for model in self.querySet:
			targets.append(model.classification)

		return numpy.array(targets)

	def _none_to_0(self, data_point):
			if data_point == None:
				data_point = '0'
			return data_point
