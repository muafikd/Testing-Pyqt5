from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget,
                                QLabel, QVBoxLayout, QPushButton, 
                                QRadioButton, QButtonGroup)

app = QApplication([])
window = QWidget()

window.setWindowTitle("Тест Новый  год 2021")
window.show()
#------------------
line = QVBoxLayout()
vline = QVBoxLayout()

label = QLabel('символ года 2021?')
vline.addWidget(label,  alignment=Qt.AlignHCenter )
radio1 = QRadioButton('год Быка')
radio2 = QRadioButton('год Змеи')
radio3 = QRadioButton('год Лошади')

rgroup = QButtonGroup()
rgroup.addButton(radio1, id = 1)
rgroup.addButton(radio2, id = 2)
rgroup.addButton(radio3, id = 3)

line.addWidget(radio1)
line.addWidget(radio2)
line.addWidget(radio3)

vline.addLayout(line)

button = QPushButton('Следующий вопрос')
vline.addWidget(button, alignment=Qt.AlignHCenter)


def show_result(result):
    label.hide()
    radio1.hide()
    radio2.hide()
    radio3.hide()
    button.hide()
    score = QLabel("Ты набрал: " + str(result))
    vline.addWidget(score, alignment = Qt.AlignCenter)

def check_second(result):
    if rgroup.checkedId() == 1:
        result = result + 0
    elif rgroup.checkedId() == 2:
        result = result + 50
    elif rgroup.checkedId() == 3:
        result = result + 0
    show_result(result)

def next_question(result):
    label.setText('Какое у тебя настроение?')
    radio1.setText('Не очень...')
    radio2.setText('Новогоднее')
    radio3.setText('Спать хочу')
    button.clicked.connect(lambda: check_second(result))

def check(result = 0):
    if rgroup.checkedId() == 1:
        result = result + 50
    elif rgroup.checkedId() == 2:
        result = result + 0
    elif rgroup.checkedId() == 3:
        result = result + 0
    next_question(result)

button.clicked.connect(check)


window.setLayout(vline)
#-------------------------------------------------

app.exec_()
