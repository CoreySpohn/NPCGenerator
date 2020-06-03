import random
class Race():
	def __init__(self):
		self.race = 'Default race'
		self.test = 'This is a test'
		self.age = '0'

	def gen_name(self, gender):
		return 'Name'

	def gen_age(self):
		return str(random.randint(0,500))

	def gen_motivation(self):
		return 'Nothing now'