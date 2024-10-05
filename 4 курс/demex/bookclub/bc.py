#  widget - это имя, присваиваемое компоненту пользовательского интерфейса,
#  с которым пользователь может взаимодействовать 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QApplication, # это то, что поддерживает работоспособность приложения Qt, выполняя его основной цикл событий
    QDialog # это базовый класс диалогового окна
)

from PyQt5.uic import loadUi # загрузка интерфейса, созданного в Qt Creator

import sys # взаимодействие с интерпретатором

from PyQt5.QtGui import QPixmap, QIcon # для работы с изображениями и загрузки иконок

import sqlite3

from user import UserScreen

# Окно приветствия
class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("test.ui",self) # загружаем интерфейс
   
# запуcк приложения
app = QApplication(sys.argv)

# позволяте менять страницы в окне
welcome = WelcomeScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)

# загружаем иконку
icon = QIcon()
icon.addPixmap(QPixmap("logo.png"), QIcon.Normal, QIcon.Off)
widget.setWindowIcon(icon) 
widget.show()

# запускаем приложение
try:
    sys.exit(app.exec_())
except:
    print("You close application")