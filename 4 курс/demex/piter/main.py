from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap, QIcon # для работы с изображениями и загрузки иконок

import sys

from welcomeScreen import welcomeScreen

app = QApplication(sys.argv)

welcome = welcomeScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)

icon = QIcon()
icon.addPixmap(QPixmap("media/logo.png"), QIcon.Normal, QIcon.Off)
widget.setWindowIcon(icon)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print('закрыто')