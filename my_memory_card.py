from random import shuffle
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
#helloy

def reg():
    gb2.hide()
    gb1.show()
    
    
def back_reg():
    gb1.hide()
    gb2.show()

def join():
    gb2.hide()
    gb1.show()
    confirm_password.hide()

def back_join():
    gb1.hide()
    gb2.show()
    confirm_password.show()

app = QApplication([])
win = QWidget()
win.resize(600, 400)


bl_main = QVBoxLayout()
bl_main.addStretch(1)
bl_gb = QVBoxLayout()
bl_gb.setSpacing(13)
 
#создание виджетов
login = QLineEdit()
login.setPlaceholderText('Введите логин...')

password = QLineEdit()
password.setPlaceholderText('Введите пароль...')
btn_answer = QPushButton('Готово')
btn_back = QPushButton('Назад')
    
    
confirm_password = QLineEdit()
confirm_password.setPlaceholderText('Потвердите пароль...')

btn_answer.setFixedWidth(100)
btn_back.setFixedWidth(100)
gb1 = QGroupBox('Регистрация')

#создание виджетов для второго групбокса
gb2 = QGroupBox()
r_btn1 = QPushButton('Регистрация')
r_btn2 = QPushButton('Вход')
gb2 = QGroupBox('Главное меню')
gb2.setFixedWidth(250)

bl_gb2_main = QVBoxLayout()
bl_gb2_h1 = QHBoxLayout()
bl_gb2_h2 = QHBoxLayout()
#добавление на gb2
gb2.setLayout(bl_gb2_main)
bl_gb2_main.addLayout(bl_gb2_h1)
bl_gb2_main.addLayout(bl_gb2_h2)
bl_gb2_h1.addWidget(r_btn1)
bl_gb2_h1.addWidget(r_btn2)
 
#добавление на направляющие
bl_main.addWidget(gb1)
gb1.hide()
bl_gb.addWidget(login, alignment=Qt.AlignCenter)
bl_gb.addWidget(password, alignment=Qt.AlignCenter)
bl_gb.addWidget(confirm_password, alignment=Qt.AlignCenter )
 
gb1.setLayout(bl_gb)

bl_main.addWidget(gb2, alignment=Qt.AlignCenter)
bl_main.addStretch(1)

bl_main.addWidget(btn_answer, alignment=Qt.AlignCenter)
bl_main.addWidget(btn_back, alignment=Qt.AlignRight)

r_btn1.clicked.connect(reg)
r_btn2.clicked.connect(join)
btn_back.clicked.connect(back_reg)
btn_back.clicked.connect(back_join)

win.setLayout(bl_main)
win.show()
app.exec_()
