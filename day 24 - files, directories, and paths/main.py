# read file
with open("./my_file.txt") as file:
	contents = file.read()
	print(contents)

# overwrite file contents: mode = 'w'
with open("./my_file.txt", mode="w") as file:
	file.write("Overwritten text.")

# append to file: mode = 'a'
with open("./my_file.txt", mode="a") as file:
	file.write("\nNew text.")

# create a new file and write something to it: mode must be 'w'
with open("./new_file.txt", mode="w") as file:
	file.write("Text of new file.")