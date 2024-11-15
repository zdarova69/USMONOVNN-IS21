from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (    
    QDialog, # это базовый класс диалогового окна
    QTableWidgetItem  # для работы с таблицами
)

import sqlite3

class Database():
    def __init__(self):
        self.db = 'uchet.db'

class showData(Database):
    def __init__(self):
        super().__init__()  # Вызываем конструктор базового класса
        pass

    def execute_query(self, query, params=None):
        conn = sqlite3.connect(self.db)
        cur = conn.cursor()
        if params:
            data = cur.execute(query, params)
        else:
            data = cur.execute(query)
        col_names = [i[0] for i in data.description]
        data_rows = data.fetchall()
        conn.commit()
        conn.close()
        return col_names, data_rows
        
class showSelect(showData):
    def __init__(self):
        super(showSelect, self).__init__()

        # self.showdata()

    def showdata(self, table_widget, zapros, userID=None):
        if userID is not None:
            col_names, data_rows = self.execute_query(zapros, (userID[0],))
        else:
            col_names, data_rows = self.execute_query(zapros)
        
        table_widget.setColumnCount(len(col_names))
        table_widget.setHorizontalHeaderLabels(col_names)
        table_widget.setRowCount(0)

        for i, row in enumerate(data_rows):
            table_widget.setRowCount(table_widget.rowCount() + 1)
            for j, elem in enumerate(row):
                table_widget.setItem(i, j, QTableWidgetItem(str(elem)))

        table_widget.resizeColumnsToContents()
        print('столбцов ',len(col_names))
        return len(col_names)


# class insertData(Database):
#     def __init__(self, line_edits):
#         # Сохранение массива QLineEdit в словарь
#         self.fields_dict = {
#             'IDrequest': line_edits[0],
#             'startDate': line_edits[1],
#             'orgTechTypeID': line_edits[2],
#             'orgTechModel': line_edits[3],
#             'problemDescryption': line_edits[4],
#             'requestStatusID': line_edits[5],
#             'completionDate': line_edits[6],
#             'repairParts': line_edits[7],
#             'masterID': line_edits[8],
#             'clientID': line_edits[9]
#         }

#         # Инициализация кнопки
#         self.SaveButton = self.findChild(QPushButton, 'SaveButton')

#     def set_fields_from_kwargs(self, **kwargs):
#         # Установка значений в соответствующие поля
#         for key, value in kwargs.items():
#             if key in self.fields_dict:
#                 self.fields_dict[key].setText(str(value))