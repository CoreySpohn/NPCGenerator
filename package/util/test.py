import markov_gen as mg
import numpy as np

file = np.genfromtxt('names.txt', delimiter=',', dtype=str)
human_generator = mg.NameGenerator(file)
print(human_generator.generate())