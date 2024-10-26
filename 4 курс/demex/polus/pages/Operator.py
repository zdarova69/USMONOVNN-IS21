from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (    
    QDialog, # это базовый класс диалогового окна
    QTableWidgetItem  # для работы с таблицами
)

import sqlite3

class Operator(QDialog):
    def __init__(self, table_widget):        
        super(Operator, self).__init__()
        print("Проверка открытия страницы оператора")
        self.tableVseZayavki = table_widget
        print(self.tableVseZayavki)
        print(table_widget)
        self.showdata()

    def showdata(self):
        conn1 = sqlite3.connect("uchet.db")
        cur1 = conn1.cursor()
        data = cur1.execute(f"""SELECT
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
                                    users c ON r.clientID = c.IDuser;""")
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