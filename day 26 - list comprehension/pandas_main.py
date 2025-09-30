import pandas

students_dict = {
	'student': ['Angela', 'James', 'Lily'],
	'score': [56, 76, 98]
}

# convert dictionary into data frame
students_data_frame = pandas.DataFrame(students_dict)

# check data type
print(type(students_data_frame))
print(type(students_data_frame.student))

for (index, row) in students_data_frame.iterrows():
	# return values of the student column
	print(row.student)
	
	# return values of the score column
	print(row.score)
	
	# return score of a given student
	if row.student == 'Lily':
		print(row.score)