#  widget - это имя, присваиваемое компоненту пользовательского интерфейса,
#  с которым пользователь может взаимодействовать 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QApplication, # это то, что поддерживает работоспособность приложения Qt, выполняя его основной цикл событий
)

import sys # взаимодействие с интерпретатором

from PyQt5.QtGui import QPixmap, QIcon # для работы с изображениями и загрузки иконок

from pages.WelcomeScreen import AuthPage, UserScreen

class Program(AuthPage, UserScreen):
    def __init__(self):
        super().__init__()
        self.SignInButton.clicked.connect(self.check_user)  # нажатие на кнопку и вызов функции

# запуcк приложения
app = QApplication(sys.argv)

# позволяте менять страницы в окне
welcome = Program()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)

# загружаем иконку
icon = QIcon()
icon.addPixmap(QPixmap("media/logo.png"), QIcon.Normal, QIcon.Off)
widget.setWindowIcon(icon) 
widget.show()

# запускаем приложение
try:
    sys.exit(app.exec_())
except:
    print("You close application")