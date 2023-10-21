from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from data import Question, QuestionView
from random import shuffle
app = QApplication([])

from main_window import *   
qst1 = Question("Якесь питання", "правильна відповідь", "не правильно", "теж не правильно", "і ця не правильно")


radio_list = [btn1, btn2, btn3, btn4]
shuffle(radio_list)

form_card = QuestionView(qst1, question, radio_list[0], radio_list[1], radio_list[2], radio_list[3])
form_card.show
win_card.show()
app.exec_()