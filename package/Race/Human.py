from package.Race.Race import Race
import random

class Human(Race):
	def __init__(self):
		self.race = 'Human'

	def gen_name(self):
		names = ['Name 1', 'Name 2', 'Name 3']
		name = random.choice(names)
		return name

	# def gen_age(self):
	# 	return str(random.randint(0,500))
