from PyQt5 import QtWidgets

from PyQt5.QtWidgets import QApplication, QDialog

from PyQt5.QtGui import QPixmap, QIcon # для работы с изображениями и загрузки иконок
from PyQt5.uic import loadUi

from modules.admin import admin
from modules.elder import elder
from modules.saler import saler
import sqlite3
class welcomeScreen(QDialog):
    def __init__(self, ) -> None:
        super(welcomeScreen, self).__init__()
        loadUi('ui/dialog.ui', self)
        self.password_field.setEchoMode(QtWidgets.QLineEdit.Password)
        self.sign_in_button.clicked.connect(self.sign_up_function)
        self.sign_out_button.clicked.connect(self.sign_out)
        self.sign_out_button.hide()
        self.stackedWidget.currentChanged.connect(self.on_page_changed)
    def sign_up_function(self):
        login = self.login_edit.text()
        password = self.password_field.text()

        conn = sqlite3.connect('try3.db')
        cur = conn.cursor()
        cur.execute('select type_worker from worker where login = ? and password = ?', (login, password))
        type_user = cur.fetchone()
        if type_user:
            print(type_user)
            if type_user[0]==1:
                self.stackedWidget.setCurrentWidget(self.saler)
                dasd = saler()
            elif type_user[0]==2:
                self.stackedWidget.setCurrentWidget(self.admin)
                dasd = admin()
            elif type_user[0]==3:
                self.stackedWidget.setCurrentWidget(self.elder)
                dasd = elder()
        else:
            self.error_field.setText('неправильный пароль')
        
        conn.commit
    def on_page_changed(self, index):
        if index == self.stackedWidget.indexOf(self.auth):
            self.sign_out_button.hide() 
        else:
            self.sign_out_button.show()
    def sign_out(self):
        self.stackedWidget.setCurrentWidget(self.auth)
    