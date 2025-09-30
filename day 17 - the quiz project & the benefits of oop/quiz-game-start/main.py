from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
		question_bank.append(
				Question(question['text'], question['answer'])
		)

quiz = QuizBrain(question_bank)

while quiz.still_have_questions():
	quiz.ask_question()

print("You've completed the quuiz")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")