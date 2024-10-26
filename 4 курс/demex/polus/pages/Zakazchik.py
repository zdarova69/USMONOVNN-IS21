from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (    
    QDialog, # это базовый класс диалогового окна
    QTableWidgetItem
)

import sqlite3

class Zakazchik(QDialog):
    def __init__(self, table_widget, userID):        
        super(Zakazchik, self).__init__()
        print("Проверка открытия страницы заказчика")
        self.tableZakazchikaZayavki = table_widget
        print(self.tableZakazchikaZayavki)
        print(table_widget)
        self.showdata(userID)

    def showdata(self, userID):
        conn1 = sqlite3.connect("uchet.db")
        cur1 = conn1.cursor()
        print(userID[0])
        data = cur1.execute(f"""SELECT
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
                                    WHERE r.clientID = {userID[0]};""")
        col_name = [i[0] for i in data.description]
        print(col_name)
        data_rows = data.fetchall()
        self.tableZakazchikaZayavki.setColumnCount(len(col_name))
        print(len(col_name))
        
        self.tableZakazchikaZayavki.setHorizontalHeaderLabels(col_name)
        self.tableZakazchikaZayavki.setRowCount(0)       
        for i, row in enumerate(data_rows):
            self.tableZakazchikaZayavki.setRowCount(self.tableZakazchikaZayavki.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableZakazchikaZayavki.setItem(i, j, QTableWidgetItem(str(elem)))
        self.tableZakazchikaZayavki.resizeColumnsToContents()
        conn1.commit()
        conn1.close()