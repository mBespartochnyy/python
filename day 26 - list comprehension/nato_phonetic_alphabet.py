# import modules
import pandas as pd

# import data
letter_mapping = pd.read_csv('./data/nato_phonetic_alphabet.csv')

#TODO 1. Create a dictionary in {"A": "Alfa", "B": "Bravo"} format
letter_dict = dict(zip(letter_mapping['letter'], letter_mapping['code']))

# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = input("What is your name?: ").upper().strip()

# use list comprehension to create a list of letter codes from the letter_dict dictionary
phonetic_name = [letter_dict[letter] for letter in name]
print(phonetic_name)