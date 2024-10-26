from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (    
    QDialog, # это базовый класс диалогового окна
    QTableWidgetItem
)

import sqlite3

class Master(QDialog):
    def __init__(self, table_widget):        
        super(Master, self).__init__()
        print("Проверка открытия страницы мастера")
        self.tableMasteraZayavki = table_widget
        print(self.tableMasteraZayavki)
        print(table_widget)
        self.showdata()

    def showdata(self):
        conn1 = sqlite3.connect("uchet.db")
        cur1 = conn1.cursor()
        data = cur1.execute("SELECT * FROM requests")
        col_name = [i[0] for i in data.description]
        print(col_name)
        data_rows = data.fetchall()
        self.tableMasteraZayavki.setColumnCount(len(col_name))
        print(len(col_name))
        
        self.tableMasteraZayavki.setHorizontalHeaderLabels(col_name)
        self.tableMasteraZayavki.setRowCount(0)       
        for i, row in enumerate(data_rows):
            self.tableMasteraZayavki.setRowCount(self.tableMasteraZayavki.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableMasteraZayavki.setItem(i, j, QTableWidgetItem(str(elem)))
        self.tableMasteraZayavki.resizeColumnsToContents()
        conn1.commit()
        conn1.close()