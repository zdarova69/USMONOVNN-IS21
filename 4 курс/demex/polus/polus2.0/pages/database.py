from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import sqlite3


class Database:
    def __init__(self):
        self.db = 'uchet.db'

    def connect(self):
        try:
            return sqlite3.connect(self.db)
        except sqlite3.Error as e:
            print(f"Ошибка подключения к базе данных: {e}")
            return None


class showData(Database):
    def __init__(self):
        super().__init__()  # Наследуем базу данных

    def execute_query(self, query, params=None):
        conn = self.connect()
        if conn is None:
            raise ConnectionError("Не удалось установить подключение к базе данных.")

        try:
            cur = conn.cursor()
            if params:
                data = cur.execute(query, params)
            else:
                data = cur.execute(query)

            col_names = [i[0] for i in data.description]
            data_rows = data.fetchall()
            return col_names, data_rows
        except sqlite3.Error as e:
            print(f"Ошибка выполнения запроса: {e}")
            raise
        finally:
            conn.close()

    def insert_data(self, query, params=None):
        conn = self.connect()
        if conn is None:
            raise ConnectionError("Не удалось установить подключение к базе данных.")

        try:
            conn = sqlite3.connect(self.db)
            cur = conn.cursor()
            if params:
                cur.execute(query, params)
            else:
                cur.execute(query)
            conn.commit()
        except sqlite3.Error as e:
            print(f"Ошибка выполнения запроса: {e}")
            raise
        finally:
            conn.commit()
            conn.close()
        

class showSelect(showData):
    def __init__(self):
        super().__init__()  # Наследуем функциональность выполнения запросов

    def showdata(self, table_widget, query, params=None):
        try:
            if params is not None:
                col_names, data_rows = self.execute_query(query, (params,))
            else:
                col_names, data_rows = self.execute_query(query)

            table_widget.setColumnCount(len(col_names))
            table_widget.setHorizontalHeaderLabels(col_names)
            table_widget.setRowCount(0)

            for i, row in enumerate(data_rows):
                table_widget.setRowCount(table_widget.rowCount() + 1)
                for j, elem in enumerate(row):
                    table_widget.setItem(i, j, QTableWidgetItem(str(elem)))

            table_widget.resizeColumnsToContents()
            print("Столбцов:", len(col_names))
            return len(col_names)
        except Exception as e:
            print(f"Ошибка при отображении данных: {e}")
            return 0


