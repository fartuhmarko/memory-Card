class Question():
    def __init__ (self, question, right_answer, wrong_ans_1, wrong_ans_2, wrong_ans_3):
        self.question = question
        self.right_answer = right_answer
        self.wrong_ans_1 = wrong_ans_1
        self.wrong_ans_2 = wrong_ans_2
        self.wrong_ans_3 = wrong_ans_3

        self.attemps = 0
        self.correct = 0

        self.is_active = True

    def got_right(self):
        self.correct += 1
        self.attemps += 1


    def got_wrong(self):
        self.attemps += 1

class QuestionView():
    def __init__(self, question_model, question, right_answer, wrong_ans_1, wrong_ans_2, wrong_ans_3):
        self.question = question
        self.right_answer = right_answer
        self.wrong_ans_1 = wrong_ans_1
        self.wrong_ans_2 = wrong_ans_2
        self.wrong_ans_3 = wrong_ans_3
    def change(self, question_model):
        self.question_model = question_model
        



    def show(self):
        self.question.setText(self.question_model.question)
        self.right_answer.setText(self.question_model.rignt_answer)
        self.wrong_ans_1.setText(self.question_model.wrong_ans_1)
        self.wrong_ans_2.setText(self.question_model.wrong_ans_2)
        self.wrong_ans_3.setText(self.question_model.wrong_ans_3)

