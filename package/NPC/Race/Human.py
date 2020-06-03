from package.NPC.Race.Race import Race
from package.util.gen_from_table import gen_from_table

class Human(Race):
	def __init__(self):
		self.race = 'Human'

	def gen_name(self, gender):
		# Human name generation, takes the 
		folder = 'Tables/Name/'
		base_filename = 'HumanNames'
		male_suffix_filename = 'HumanMaleSuffix'
		female_suffix_filename = 'HumanFemaleSuffix'
		first_name, last_name, male_suffix, female_suffix = gen_from_table(folder, base_filename, base_filename, male_suffix_filename, female_suffix_filename)
		# Strip the first name and then add a suffix based on gender
		vowels = ['a', 'e', 'i', 'o', 'u']
		removing_letters = True
		while removing_letters:
			# Remove the last letter because it didn't get removed last time
			first_name = first_name[:-1]
			if len(first_name) == 1:
				# If there are names without a vowel, find a new one
				first_name = gen_from_table(folder, base_filename)
			 
			if first_name[-1] in vowels:
				removing_letters = False

		if gender == 'Male':
			first_name = first_name.title() + male_suffix
		if gender == 'Female':
			first_name = first_name.title() + female_suffix


		return first_name + ' ' + last_name

	# def gen_age(self):
	# 	return str(random.randint(0,500))
