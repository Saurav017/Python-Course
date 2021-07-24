
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    # for loop to iterate over the question data
    new_question = Question(question["question"], question["correct_answer"])
    # Creating an Question object  for each entry in question data
    question_bank.append(new_question)
#     Appending each Question inside the question_bank list

quiz_game = QuizBrain(question_bank)

while quiz_game.still_has_question():
    #Loop until the question ends
    quiz_game.next_question()
#     Print questions


print("You have completed the quiz!!!!!!!")
print(f"Your final score is {quiz_game.score}/{len(question_bank)}")