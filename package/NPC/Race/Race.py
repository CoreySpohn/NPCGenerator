import random
import json
import package.util.markov_gen as markov
import numpy as np

class Race():
	def __init__(self, data):
		self.race = data["race"]
		self.max_age = data["max_age"]
		self.gen_name = markov.NameGenerator(data["names"].split(','), order=2, prior=0.001)

	def gen_age(self):
		return str(random.randint(0,500))

	def gen_motivation(self):
		return 'Nothing now'