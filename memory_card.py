from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout,
    QGroupBox, QButtonGroup, QRadioButton,
    QPushButton, QLabel)
from random import randint, shuffle


class Question():
    ''' содержит вопрос, правильный ответ и три неправильных'''

    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
        
questions_list = []
questions_list.append(
    Question('Государственный язык Бразилии', 'Португальский', 'Английский', 'Испанский', 'Бразильский'))
questions_list.append(
    Question('Какого цвета нет на флаге России?', 'Зелёный', 'Красный', 'Белый', 'Синий'))
questions_list.append(
    Question('Национальная хижина якутов', 'Ураса', 'Юрта', 'Иглу', 'Хата'))

app = QApplication([])

btn_OK = QPushButton('Ответить')  # кнопка ответа
lb_Question = QLabel('Самый сложный вопрос в мире!')  # текст вопроса

RadioGroupBox = QGroupBox("Варианты ответов")  # группа на экране для переключателей с ответами

rbtn_1 = QRadioButton('Вариант 1') #
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')

