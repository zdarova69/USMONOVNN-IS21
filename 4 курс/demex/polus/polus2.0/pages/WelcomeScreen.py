#  widget - это имя, присваиваемое компоненту пользовательского интерфейса,
#  с которым пользователь может взаимодействовать 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (    
    QDialog, # это базовый класс диалогового окна
    QTableWidget
)
from PyQt5.QtWidgets import QVBoxLayout, QLineEdit, QPushButton, QStackedWidget
from PyQt5.uic import loadUi # загрузка интерфейса, созданного в Qt Creator

import sqlite3
from datetime import date

from pages.Manager import Manager
from pages.database import showSelect


class WelcomeScreen(QDialog):
    """
    Это класс окна приветствия.
    """
    def __init__(self):
        """
        Это конструктор класса
        """
        super(WelcomeScreen, self).__init__()
        loadUi("views/welcomescreen.ui", self)  # загружаем интерфейс.
        self.AvtorButton.clicked.connect(self.sign_out)
        self.AvtorButton.hide()
        self.stackedWidget.currentChanged.connect(self.hiddenButton)  


    def hiddenButton(self):
        if self.stackedWidget.currentWidget() == self.Avtorisation:  
            self.AvtorButton.hide()
        else:
            self.AvtorButton.show()

    def sign_out(self):
        self.stackedWidget.setCurrentWidget(self.Avtorisation)
        

class AuthPage(WelcomeScreen):        
    def __init__(self):
        super().__init__() 
        # Пример инициализации объектов, которые будут использоваться в AuthPage

        self.PasswordField.setEchoMode(QLineEdit.Password)  # скрываем пароль

    def signupfunction(self): # создаем функцию регистрации        
        user = self.LoginField.text() # создаем пользователя и получаем из поля ввода логина введенный текст
        password = self.PasswordField.text() # создаем пароль и получаем из поля ввода пароля введенный текст
        return user, password # выводит логин и пароль       
    
   

class UserScreen(WelcomeScreen, showSelect):
    def __init__(self):
        super().__init__()
        # self.inser_button.clicked.connect(self.execute_query())
        self.pages = {
    1: {
        'zp': "",
        'table': '',
    },
    2: {
        'zp': """SELECT 
                    r.*,  -- Выбираем все столбцы из таблицы requests
                    c.message AS "Сообщение"  -- Выбираем столбец message из таблицы comments
                FROM 
                    requests r
                JOIN 
                    comments c ON r.IDrequest = c.requestID;""",
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
                    c.fio AS "ID клиента",
                    com.message AS "Сообщение"
                FROM 
                    requests r
                LEFT JOIN 
                    orgTechTypes ot ON r.orgTechTypeID = ot.IDorgTechType
                LEFT JOIN 
                    requestStatuses rs ON r.requestStatusID = rs.IDrequestStatus
                LEFT JOIN 
                    users m ON r.masterID = m.IDuser
                LEFT JOIN 
                    users c ON r.clientID = c.IDuser
                LEFT JOIN 
                    comments com ON r.IDrequest = com.requestID;""",
    },
    4: {
        'zp': """SELECT
                    r.IDrequest AS "Идентификатор заявки", 
                    ot.orgTechType AS "ID типа техники",
                    r.orgTechModel AS "Модель техники",
                    r.problemDescryption AS "Описание проблемы",  -- Убедитесь, что это правильное название
                    rs.requestStatus AS "ID статуса заявки",
                    co.message AS "Комментарий"
                FROM 
                    requests r
                LEFT JOIN 
                    orgTechTypes ot ON r.orgTechTypeID = ot.IDorgTechType
                LEFT JOIN 
                    requestStatuses rs ON r.requestStatusID = rs.IDrequestStatus
                LEFT JOIN 
                    comments co ON r.IDrequest = co.requestID
                WHERE 
                    r.clientID = ?;""",
        "insert": """INSERT or IGNORE INTO requests (IDrequest, orgTechTypeID, orgTechModel, problemDescryption, requestStatusID, startDate, clientID)
                VALUES (?, ?, ?, ?, ?, ?, ?);"""
    }
}   
        self.insert_button.clicked.connect(self.insert)  # нажатие на кнопку и вызов функци
        # Создаем пустой список для хранения QLineEdit
    def hide_label(self, count):
        line_edits = []
        # Проходим по всем элементам в QVBoxLayout
        for i in range(self.verticalLayout_3.count()):
            item = self.verticalLayout_3.itemAt(i)
            widget = item.widget()
            widget.hide()
            
            # Проверяем, является ли виджет QLineEdit
            if isinstance(widget, QLineEdit):
                line_edits.append(widget)
        # Теперь line_edits содержит список всех QLineEdit в QVBoxLayout
        self.lines = line_edits[count:]
        for i in line_edits[count:]:
            i.show()
    def check_user(self):
        user, password = self.signupfunction()
        print(user, password)
        if len(user)==0 or len(password)==0: # если пользователь оставил пустые поля
            self.ErrorField.setText("Заполните все поля") # выводим ошибку в поле
        else:
            self.ErrorField.setText(" ") # выводим ошибку в поле
            conn = sqlite3.connect("uchet.db") # подключение к базе данных в () изменить на название своей БД
            cur = conn.cursor() # переменная для запросов

            cur.execute('SELECT typeID FROM users WHERE login=(?) and password=(?)', [user, password]) # получаем тип пользователя, логин и пароль которого был введен
            self.typeUser = cur.fetchone()[0] # получает только один тип пользователя
            print(self.typeUser)
            if self.typeUser == None:
                self.ErrorField.setText("Пользователь с такими данными не найден")
            else:
                if self.typeUser == 1:
                    cols = Manager()
                else:
                    if self.typeUser == 4:
                        cur.execute('SELECT IDuser FROM users WHERE login=(?) and password=(?)', [user, password])
                        userID = cur.fetchone()  # Получаем кортеж с ID пользователя

                        cols = self.showdata(self.tableMasteraZayavki, query=self.pages[self.typeUser]['zp'], params=userID[0],) 
                        self.userID = userID[0]
                    else:
                        cols = self.showdata(self.tableMasteraZayavki, query=self.pages[self.typeUser]['zp'])    
                
                
                    self.hide_label(11-cols)

                self.table = self.findChild(QTableWidget, 'tableWidget')
                self.stackedWidget.setCurrentWidget(self.user)

                conn.commit() # сохраняет в подключении запросы
                conn.close() # закрываем подключение

    def insert(self):
        if self.typeUser == 4:
            # Создаем список значений из текста каждой строки
            values = [i.text() for i in self.lines]

            # Добавляем текущую дату и self.typeUser в список
            current_date = date.today().strftime("%Y-%m-%d")
            values.append(current_date)
            values.append(self.userID)
            self.insert_data(query=self.pages[self.typeUser]['insert'], params=values)
            self.showdata(self.tableMasteraZayavki, query=self.pages[self.typeUser]['zp'], params=self.userID,) 