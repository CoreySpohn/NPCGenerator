from package.Race.Race import Race
from package.Race.Human import Human

class NPC():
    def __init__(self, race_odds):
    	self.race_odds = race_odds
    	self.gen_race()
    	self.name = 'Test name'

    def gen_race(self):
    	self.race = Human()

    def gen_name(self):
    	self.name = self.race.gen_name()

    def gen_age(self):
    	self.age = self.race.gen_age()

    # def gen_name(self):
    # 	self.name='Corey'	