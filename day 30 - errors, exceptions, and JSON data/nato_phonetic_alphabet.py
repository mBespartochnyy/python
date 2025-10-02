# import modules
import pandas as pd

# import data
letter_mapping = pd.read_csv('../day 26 - list comprehension/data/nato_phonetic_alphabet.csv')

# config
done = False

# zip function pairs values from multiple iterables like lists, tuples, or pandas series into a tuple
# in this case, I paired letters and code into a tuple ('A', 'Alpha') and then converted result into a
# dictionary
letter_dict = dict(zip(letter_mapping['letter'], letter_mapping['code']))

def generate_phonetics():
	# get name
	name = input("What is your name?: ").upper().strip()

	try:
		# check if name is valid
		phonetic_name = [letter_dict[letter] for letter in name]
	except KeyError:
		# if name is not valid, communicate that and ask for name again
		print("Sorry, only letters in the alphabet please.")
		generate_phonetics()
	else:
		# if name is valid, give result
		print(phonetic_name)

generate_phonetics()