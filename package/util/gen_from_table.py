import os, os.path
from pathlib import Path
import random
script_dir = Path(os.path.dirname(__file__))
package_dir = script_dir.parent

def gen_from_table(folder, *args):
	'''
	The args are a list of lists, where each sublist is [folder, filename]
	for a random table
	'''
	output = []
	for filename in args:
		path = os.path.join(package_dir, folder+str(filename)+'.txt')
		output.append(random.choice(open(path).readlines()).strip('\n'))
	return output
