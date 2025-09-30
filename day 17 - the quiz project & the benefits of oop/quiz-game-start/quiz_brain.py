class QuizBrain:
	def __init__(self, question_list: list) -> None:
		self.question_number = 0
		self.question_list = question_list
		self.score = 0
	
	def still_have_questions(self) -> bool:
		return self.question_number < len(self.question_list)
	
	def check_answer(self, correct_answer: str, user_answer: str) -> None:
		if user_answer.lower() == correct_answer.lower():
			self.score += 1
			print("You got it right!")
		else:
			print("That's wrong.")

	def ask_question(self) -> None:
		question = self.question_list[self.question_number]
		self.question_number += 1
		user_answer = input(f"Q.{self.question_number}: {question.text}. (True/False)?: ")
		print(f"Your answer: {user_answer.lower()}")
		print(f"correct answer: {question.answer.lower()}")
		self.check_answer(question.answer, user_answer)
		print(f"Your current score is: {self.score}/{self.question_number}\n")