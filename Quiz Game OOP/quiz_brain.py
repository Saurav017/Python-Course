

class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
    #   Initialising the question list to an input

    def still_has_question(self):
        """
        :return: function to return true values until the questions are remaining
        """
        # if self.question_number < len(self.question_list):
        #     return True
        # else:
        #     return False


    #     OR Method 2

        return self.question_number < len(self.question_list)


    def next_question(self):
        current_question = self.question_list[self.question_number]
    #   Retrieving the current question from the question list

        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False) ?")
    #   Input() function to show the current question text and ask question
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):

        """

        :param user_answer:
        :param correct_answer:
        :return:Check whether the answer is correct or not and change the score according to that
        """
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong!")
        print(f"The correct answer is {correct_answer}")
        print(f"Your score is {self.score}/{self.question_number}")
        print("\n")

