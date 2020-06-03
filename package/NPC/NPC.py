from package.NPC.Race.Race import Race
from package.NPC.Race.Human import Human
import random

class NPC():
    def __init__(self, race_odds):
    	self.race_odds = race_odds
    	self.gen_race()
    	self.gender = 'Male'
    	self.name = 'Test name'

    def gen_race(self):
    	self.race = Human()

    def gen_gender(self):
    	self.gender = random.choice(['Male', 'Female'])

    def gen_name(self):
    	self.name = self.race.gen_name(self.gender)

    def gen_age(self):
    	self.age = self.race.gen_age()

    # def gen_name(self):
    # 	self.name='Corey'	