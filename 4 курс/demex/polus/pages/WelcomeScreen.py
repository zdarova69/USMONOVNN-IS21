#  widget - это имя, присваиваемое компоненту пользовательского интерфейса,
#  с которым пользователь может взаимодействовать 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (    
    QDialog, # это базовый класс диалогового окна
    QTableWidget
)
from PyQt5.QtWidgets import QVBoxLayout, QLineEdit

from PyQt5.uic import loadUi # загрузка интерфейса, созданного в Qt Creator

import sqlite3

from pages.Manager import Manager
from pages.UserTableDialog import UserTableDialog



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
        loadUi("views/welcomescreen.ui",self) # загружаем интерфейс.
        self.PasswordField.setEchoMode(QtWidgets.QLineEdit.Password) # скрываем пароль
        self.SignInButton.clicked.connect(self.signupfunction) # нажати на кнопку и вызов функции
        # Подключение кнопок к методам переключения страниц с использованием lambda
        #self.SignInButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Zakazchik))
        self.AvtorButton.clicked.connect(self.sign_out)
        self.AvtorButton.hide()
        self.stackedWidget.currentChanged.connect(self.hiddenButton)     
        
        
        self.pages = {
    1: {
        'zp': "",
        'table': '',
        'widget': self.Manager
    },
    2: {
        'zp': "SELECT * FROM requests",
        'table': 'tableWidget',
        'widget': self.Master,
        'columns': 0
    },
    3: {
        'zp': """SELECT
            r.IDrequest AS "Идентификатор заявки",
            r.startDate AS "Дата начала заявки",
            ot.orgTechType AS "ID типа техники",
            r.orgTechModel AS "Модель техники",
            r.problemDescryption AS "Описание проблемы",
            rs.requestStatus AS "ID статуса заявки",
            r.completionDate AS "Дата завершения",
            r.repairParts AS "Замененные запчасти",
            m.fio AS "ID мастера",
            c.fio AS "ID клиента"
            FROM 
                requests r
            LEFT JOIN 
                orgTechTypes ot ON r.orgTechTypeID = ot.IDorgTechType
            LEFT JOIN 
                requestStatuses rs ON r.requestStatusID = rs.IDrequestStatus
            LEFT JOIN 
                users m ON r.masterID = m.IDuser
            LEFT JOIN 
                users c ON r.clientID = c.IDuser;""",

        'table': 'tableWidget',
        'widget': self.Master,
        'columns': 0
    },
    4: {
        'zp': """SELECT
            r.IDrequest AS "Идентификатор заявки", 
            ot.orgTechType AS "ID типа техники",
            r.orgTechModel AS "Модель техники",
            r.problemDescryption AS "Описание проблемы",
            rs.requestStatus AS "ID статуса заявки"  
            FROM 
                requests r
            LEFT JOIN 
                orgTechTypes ot ON r.orgTechTypeID = ot.IDorgTechType
            LEFT JOIN 
                requestStatuses rs ON r.requestStatusID = rs.IDrequestStatus
            WHERE r.clientID = ?;""",
        'table': 'tableWidget',
        'widget': self.Master,
        'columns': 5
    }
}
        # Создаем пустой список для хранения QLineEdit
        self.line_edits = []
    def hide_label(self, count):
        # Проходим по всем элементам в QVBoxLayout
        for i in range(self.verticalLayout_3.count()):
            item = self.verticalLayout_3.itemAt(i)
            widget = item.widget()
            widget.hide()
            
            # Проверяем, является ли виджет QLineEdit
            if isinstance(widget, QLineEdit):
                self.line_edits.append(widget)
        # Теперь line_edits содержит список всех QLineEdit в QVBoxLayout
        for i in self.line_edits[count:]:
            i.show()
    def signupfunction(self): # создаем функцию регистрации
        
        user = self.LoginField.text() # создаем пользователя и получаем из поля ввода логина введенный текст
        password = self.PasswordField.text() # создаем пароль и получаем из поля ввода пароля введенный текст
        print(user, password) # выводит логин и пароль

        if len(user)==0 or len(password)==0: # если пользователь оставил пустые поля
            self.ErrorField.setText("Заполните все поля") # выводим ошибку в поле
        else:
            self.ErrorField.setText(" ") # выводим ошибку в поле
            conn = sqlite3.connect("uchet.db") # подключение к базе данных в () изменить на название своей БД
            cur = conn.cursor() # переменная для запросов

            cur.execute('SELECT typeID FROM users WHERE login=(?) and password=(?)', [user, password]) # получаем тип пользователя, логин и пароль которого был введен
            typeUser = cur.fetchone() # получает только один тип пользователя
            print(typeUser)
            if typeUser == None:
                self.ErrorField.setText("Пользователь с такими данными не найден")
            elif typeUser[0] == 1:
                self.lybaya = Manager()
            else:
                self.table = self.findChild(QTableWidget, self.pages[typeUser[0]]['table'])
                self.stackedWidget.setCurrentWidget(self.pages[typeUser[0]]['widget'])
                if typeUser[0] == 4:
                    cur.execute('SELECT IDuser FROM users WHERE login=(?) and password=(?)', [user, password])
                    userID = cur.fetchone()  # Получаем кортеж с ID пользователя

                    self.lybaya = UserTableDialog(self.tableMasteraZayavki, zapros=self.pages[typeUser[0]]['zp'], userID=userID, type_user=typeUser) 

                    self.hide_label(self.pages[typeUser[0]]['columns'])
                else:
                    self.lybaya = UserTableDialog(self.tableMasteraZayavki, zapros=self.pages[typeUser[0]]['zp'], type_user=typeUser)    
                    self.hide_label(self.pages[typeUser[0]]['columns'])

                self.stackedWidget.setCurrentWidget(self.pages[typeUser[0]]['widget'])
           
            conn.commit() # сохраняет в подключении запросы
            conn.close() # закрываем подключение
    
    def hiddenButton(self):
        if self.stackedWidget.currentWidget() == self.Avtorisation:  
            self.AvtorButton.hide()
        else:
            self.AvtorButton.show()


    def sign_out(self):
        self.stackedWidget.setCurrentWidget(self.Avtorisation)