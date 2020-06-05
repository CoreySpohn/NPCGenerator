from package.NPC.Race.Race import Race
from package.NPC.Race.Human import Human
import random
import json
import numpy as np
import os, os.path
script_dir = os.path.dirname(__file__)

class NPC():
    def __init__(self):
    	# self.race_odds = race_odds
    	# Get all of the races initialized
    	races_filename = f'{script_dir}/races.json'
    	with open(races_filename) as f:
    		race_data = json.load(f)
    	self.races = []
    	self.race_odds = []
    	for race in race_data['races']:
    		self.races.append(Race(race))
    		self.race_odds.append(race['odds'])
    	print(self.races)
    	print(self.race_odds)
    	self.gen_race()
    	self.gender = 'Male'
    	self.name = 'Test name'

    def gen_race(self):
    	self.race = np.random.choice(self.races, p=self.race_odds)

    def gen_gender(self):
    	self.gender = random.choice(['Male', 'Female'])

    def gen_name(self):
    	self.name = self.race.gen_name.generate().title()

    def gen_age(self):
    	self.age = self.race.gen_age()

    # def gen_name(self):
    # 	self.name='Corey'	