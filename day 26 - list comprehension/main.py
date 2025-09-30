import random
new_range = [num * 2 for num in range(1, 5)]
print(new_range)

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
student_scores = {
	student:random.randint(1, 100)
	for student in names
}
passed_students = {
	student: score
	for (student, score) in student_scores.items()
	if score >= 60
}
print(student_scores)
print(passed_students)