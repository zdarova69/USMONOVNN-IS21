from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (    
    QDialog, # это базовый класс диалогового окна
    QTableWidgetItem  # для работы с таблицами
)

import sqlite3

class UserTableDialog(QDialog):
    def __init__(self, table_widget, zapros, type_user,userID=None):        
        super(UserTableDialog, self).__init__()
        print("Проверка открытия страницы оператора")
        self.table = table_widget
        self.zapros = zapros
        self.userID = userID
        self.type_user = type_user
        print(self.table)
        print(table_widget)
        self.showdata()
        

    def showdata(self):
        conn1 = sqlite3.connect("uchet.db")
        cur1 = conn1.cursor()
        if self.userID is not None:
            data = cur1.execute(self.zapros, (self.userID[0],))  # Передаем userID как кортеж
        else:
            data = cur1.execute(self.zapros)
        col_name = [i[0] for i in data.description]
        print(col_name)
        data_rows = data.fetchall()
        self.table.setColumnCount(len(col_name))
        print(len(col_name))
        
        self.table.setHorizontalHeaderLabels(col_name)
        self.table.setRowCount(0)       
        for i, row in enumerate(data_rows):
            self.table.setRowCount(self.table.rowCount() + 1)
            for j, elem in enumerate(row):
                self.table.setItem(i, j, QTableWidgetItem(str(elem)))
        self.table.resizeColumnsToContents()
        conn1.commit()
        conn1.close()

    
        