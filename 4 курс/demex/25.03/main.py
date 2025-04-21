import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QListWidgetItem, 
                            QLabel, QMessageBox, QLineEdit, QTableWidgetItem)
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import Qt, QSize
from PyQt5.uic import loadUi

from database import DatabaseHandler

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Загрузка интерфейса
        loadUi('dialog.ui', self)
        
        # Настройка окна
        self.setWindowIcon(QIcon('logo.ico'))
        self.setMinimumSize(800, 600)
        self.logoLabel.setPixmap(QPixmap('logo.png').scaled(
            100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        
        # Инициализация БД
        self.db = DatabaseHandler()
        
        # Начальное состояние
        self.stackedWidget.setCurrentIndex(0)
        self.is_editing = False
        self.current_inn = None
        
        # Подключение сигналов
        self.btnAddPartner.clicked.connect(self.show_add_page)
        self.btnBack.clicked.connect(self.show_partners_page)
        self.btnSave.clicked.connect(self.save_partner)
        self.btnHistory.clicked.connect(self.show_sales_history)
        self.listPartners.itemDoubleClicked.connect(self.edit_partner)
        
        self.btnHistory.hide()

        # Инициализация данных
        self.init_combobox()
        self.load_partners()

    def init_combobox(self):
        """Инициализация комбобокса типами партнеров"""
        try:
            types = self.db.get_partner_types()
            self.typeCombo.addItems(types)
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", str(e))

    def load_partners(self):
        """Загрузка списка партнеров"""
        try:
            self.listPartners.clear()
            partners = self.db.get_partners()
            
            for partner in partners:
                item = QListWidgetItem()
                item.setData(Qt.UserRole, partner[0])
                widget = QLabel(self.format_partner_html(partner))
                widget.setContentsMargins(10, 10, 10, 10)
                widget.setStyleSheet("background-color: white;")
                self.listPartners.addItem(item)
                self.listPartners.setItemWidget(item, widget)
                item.setSizeHint(widget.sizeHint())
                
        except Exception as e:
            QMessageBox.warning(self, "Ошибка", str(e))

    def format_partner_html(self, partner):
        """Форматирование данных для отображения с проверкой на None"""
        discount = min(20, partner[3] * 2)
        director = " ".join(filter(None, [
            str(partner[9]) if partner[9] else None,
            str(partner[10]) if partner[10] else None,
            str(partner[11]) if partner[11] else None
        ])).strip()
        
        phone = str(partner[12]) if partner[12] else "Телефон не указан"
        partner_type = str(partner[14]) if partner[14] else "Тип не указан"
        
        return f"""
        <div style='font-size:14pt;'>
         <table width='100%'>
                <tr>
                    <td style='width: 70%;'><b>{partner[14]}</b> | {partner[1]} </td>
                    <td style='width: 30%; text-align: right;'>
                        <span style='color:#333;'>{discount}%</span>
                    </td>
                </tr>
            </table>
        </div>
        <div style='font-size:10pt; color:#666; margin-top:8px; line-height:1.4; 
                    white-space: normal; word-wrap: break-word;'>
            <div>{director}</div>
            <div>{phone}</div>
            <div>Рейтинг: {partner[3]}</div>
        </div>
        <div>
            <br>
            <br>
        </div>
        """

    def show_add_page(self):
        """Показать форму добавления"""
        self.clear_form()
        self.stackedWidget.setCurrentIndex(1)

    def show_partners_page(self):
        """Вернуться к списку партнеров"""
        self.stackedWidget.setCurrentIndex(0)
        self.load_partners()
        self.btnHistory.hide()
    def edit_partner(self, item):
        """Редактирование партнера"""
        inn = item.data(Qt.UserRole)
        self.btnHistory.show()
        try:
            partner = self.db.get_partner(inn)
            if not partner:
                QMessageBox.warning(self, "Ошибка", "Партнер не найден")
                return
                
            self.fill_form(partner)
            self.is_editing = True
            self.current_inn = inn
            self.innInput.setEnabled(False)
            self.stackedWidget.setCurrentIndex(1)
            
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", str(e))

    def fill_form(self, partner):
        """Заполнение формы данными с проверкой на None"""
        def safe_set_text(widget, value):
            widget.setText(str(value) if value is not None else "")
        
        safe_set_text(self.innInput, partner['inn'])
        safe_set_text(self.nameInput, partner['name'])
        self.typeCombo.setCurrentText(partner['type'] if partner['type'] else "")
        self.ratingSpin.setValue(partner['rating'])
        
        safe_set_text(self.indexInput, partner['index'])
        safe_set_text(self.regionInput, partner['region'])
        safe_set_text(self.cityInput, partner['city'])
        safe_set_text(self.streetInput, partner['street'])
        safe_set_text(self.houseInput, partner['house'])
        
        safe_set_text(self.lastNameInput, partner['last_name'])
        safe_set_text(self.firstNameInput, partner['first_name'])
        safe_set_text(self.middleNameInput, partner['middle_name'])
        safe_set_text(self.phoneInput, partner['phone'])
        safe_set_text(self.emailInput, partner['email'])

    def clear_form(self):
        """Очистка формы"""
        self.is_editing = False
        self.current_inn = None
        self.innInput.setEnabled(True)
        for widget in self.pageAddPartner.findChildren(QLineEdit):
            widget.clear()
        self.ratingSpin.setValue(0)
        self.typeCombo.setCurrentIndex(0)
    def show_sales_history(self):
        self.stackedWidget.setCurrentIndex(2)  # Переключаемся на новую страницу
        sales = self.db.load_sales_history(self.current_inn)

        try:
            if not sales:
                QMessageBox.information(None, "История реализации", "У партнера нет истории продаж.", QMessageBox.Ok)
                return

            col_names = [i[0] for i in sales.description]
            data_rows = sales.fetchall()

            self.tableWidget.setColumnCount(len(col_names))
            self.tableWidget.setHorizontalHeaderLabels(col_names)
            self.tableWidget.setRowCount(0)

            for i, row in enumerate(data_rows):
                self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))

            self.tableWidget.resizeColumnsToContents()
            print("Столбцов:", len(col_names))
            return len(col_names)
        except Exception as e:
            print(f"Ошибка при загрузке истории продаж: {e}")
            QMessageBox.critical(None, "Ошибка", f"Не удалось загрузить историю продаж. Подробности: {e}", QMessageBox.Ok)

    def save_partner(self):
        """Сохранение партнера"""
        try:
            data = self.validate_input()
            
            if self.is_editing:
                data['inn'] = self.current_inn
                self.db.save_partner(data, is_editing=True)
                message = "Данные успешно обновлены"
            else:
                self.db.save_partner(data)
                message = "Партнер успешно добавлен"
                
            QMessageBox.information(self, "Успех", message)
            self.clear_form()
            self.show_partners_page()
            
        except ValueError as e:
            QMessageBox.warning(self, "Ошибка", str(e))
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", str(e))

    def validate_input(self):
        """Проверка введенных данных"""
        errors = []
        data = {
            'inn': self.innInput.text().strip(),
            'name': self.nameInput.text().strip(),
            'type': self.typeCombo.currentText(),
            'rating': self.ratingSpin.value(),
            'index': self.indexInput.text().strip(),
            'region': self.regionInput.text().strip(),
            'city': self.cityInput.text().strip(),
            'street': self.streetInput.text().strip(),
            'house': self.houseInput.text().strip(),
            'last_name': self.lastNameInput.text().strip(),
            'first_name': self.firstNameInput.text().strip(),
            'middle_name': self.middleNameInput.text().strip(),
            'phone': self.phoneInput.text().strip(),
            'email': self.emailInput.text().strip(),
        }

        if not self.is_editing:
            if len(data['inn']) != 12 or not data['inn'].isdigit():
                errors.append("ИНН должен содержать 12 цифр")
        
        if not data['name']:
            errors.append("Укажите наименование партнера")
            
        if not data['phone'] and not data['email']:
            errors.append("Укажите телефон или email")
            
        if errors:
            raise ValueError("\n".join(errors))
            
        # Очистка пустых полей
        for key in data:
            if data[key] == "":
                data[key] = None
                
        return data

    def closeEvent(self, event):
        self.db.close()
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setFont(QFont('Segoe UI', 10))
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())