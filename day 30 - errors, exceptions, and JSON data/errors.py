# file not found
with open('a_file.txt') as file:
	file.read()

# key error
a_dictionary = {'key': 'value'}
value = a_dictionary['wrong_key']

# index error
fruit_list = ['apple', 'banana', 'pear']
fruit = fruit_list[3]

# type error
text = 'abc'
print(text + 5)

# error handling syntax
try:
	# something that migh cause an error
except:
	# do this if there was an error
else:
	# do this if there were no errors
finally:
	# do this no matter what happens