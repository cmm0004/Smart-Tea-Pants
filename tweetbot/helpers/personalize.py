import datetime
from tweetbot.models import User, Tea

class WeekDayAware(object):

	def __init__(self):
		self.weekdays = ['monday', 'tuesday', 'wednesday',
		 'thursday', 'friday', 'saturday', 'sunday']
		self.today = datetime.datetime.today()
		self.today_int = self.today.weekday()
		self.today_str = self.weekdays[self.today_int]
		self.month_int = self.today.month

	def ff_get_status(self):
		users = User.objects.filter(classification='individual')
		if len(users) > 0:
			screennames = []
			for user in users:
				screennames.append('@' + user.screen_name)
			
			ff_status = "Happy #FF "
			while len(ff_status) < 140:
				if len(screennames) > 0:
					ff_status += screennames.pop()
					ff_status += " "
					continue
				break
			print('status for ff: ' + ff_status)
			return ff_status
		return False

	def buy_individual_status(self):
		if (self.today_int % 3) == 0:
			status = "#teasontheloose Just want one? Get a previous months' tea while supplies last here: www.teasontheloose.com/buy-individual.html"
			
			#you saved month index 0-11, datetime gives 1-12
			
			#queryObject
			teas = Tea.get_teas_available(Tea, (self.month_int - 2))
			if len(teas) == 2:
				status_followup = "www.teasontheloose.com/buy-individual.html This month's individual #teas are {} and {}".format(teas[0].name, teas[1].name)
				return status, status_followup
			print('put more teas in the database!')
		print('not the right day for individual sales tweets')
		return False, False