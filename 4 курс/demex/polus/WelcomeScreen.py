#  widget - это имя, присваиваемое компоненту пользовательского интерфейса,
#  с которым пользователь может взаимодействовать 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (    
    QDialog # это базовый класс диалогового окна
)

from PyQt5.uic import loadUi # загрузка интерфейса, созданного в Qt Creator
from modules.manager import manager
from modules.operator import operator
from modules.master import master
from modules.zakazchik import zakazchik

import sqlite3

# Окно приветствия
class WelcomeScreen(QDialog):
    """
    Это класс окна приветствия.
    """
    def __init__(self):
        """
        Это конструктор класса
        """
        super(WelcomeScreen, self).__init__()
        loadUi("welcomescreen.ui",self) # загружаем интерфейс.
        self.PasswordField.setEchoMode(QtWidgets.QLineEdit.Password) # скрываем пароль
        self.SignInButton.clicked.connect(self.sign_up_function) # нажати на кнопку и вызов функции
        self.SignOutButton.clicked.connect(self.sign_out)
        self.SignOutButton.hide()
        # self.stackedWidget.setCurrentWidget(self.Avtorisation)
        self.stackedWidget.currentChanged.connect(self.on_page_changed)
    def sign_up_function(self):
        user = self.LoginField.text()
        password = self.PasswordField.text()
        print(user, password)

        if len(user) == 0 or len(password) == 0:
            self.ErrorField.setText("Заполните все поля")
        else:
            self.ErrorField.setText("Все ок")

        conn = sqlite3.connect("uchet.db")
        cur = conn.cursor()
        cur.execute('SELECT typeID FROM users WHERE login=? and password=?', (user, password))
        typeUser = cur.fetchone()
        if typeUser:
            print(typeUser[0])
            if typeUser[0] == 1:
                self.stackedWidget.setCurrentWidget(self.Manager)
                self.lybaya = manager()
            elif typeUser[0] == 2:
                self.stackedWidget.setCurrentWidget(self.Master)
                self.lybaya = master()
            elif typeUser[0] == 3:
                self.stackedWidget.setCurrentWidget(self.Operator)
                self.lybaya = operator()
            elif typeUser[0] == 4:
                self.stackedWidget.setCurrentWidget(self.Zakazchik)
                self.lybaya = zakazchik()
        else:
            self.ErrorField.setText("Неверный логин или пароль")

        conn.commit()
        
    def on_page_changed(self, index):
        if index == self.stackedWidget.indexOf(self.Avtorisation):  # Если текущая страница - Avtorisation
            self.SignOutButton.hide()
        else:
            self.SignOutButton.show()
    def sign_out(self):
        self.stackedWidget.setCurrentWidget(self.Avtorisation)


