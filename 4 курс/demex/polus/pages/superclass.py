from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (    
    QDialog, # это базовый класс диалогового окна
    QTableWidgetItem  # для работы с таблицами
)

import sqlite3

class superClass(QDialog):
    def __init__(self, table_widget, zapros, userID=None):        
        super(superClass, self).__init__()
        print("Проверка открытия страницы оператора")
        self.tableVseZayavki = table_widget
        self.zapros = zapros
        self.userID = userID
        print(self.tableVseZayavki)
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
        self.tableVseZayavki.setColumnCount(len(col_name))
        print(len(col_name))
        
        self.tableVseZayavki.setHorizontalHeaderLabels(col_name)
        self.tableVseZayavki.setRowCount(0)       
        for i, row in enumerate(data_rows):
            self.tableVseZayavki.setRowCount(self.tableVseZayavki.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableVseZayavki.setItem(i, j, QTableWidgetItem(str(elem)))
        self.tableVseZayavki.resizeColumnsToContents()
        conn1.commit()
        conn1.close()