import sys
import re
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QListWidget,
    QLineEdit, QTextEdit, QFormLayout, QComboBox, QSpinBox, QMessageBox, QStackedWidget, QGridLayout, QFrame,
    QListWidgetItem, QTableWidget, QHeaderView, QTableWidgetItem  # Добавляем QTableWidgetItem
)
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt, QSize
import sqlite3
'''
import sqlite3

# Подключение к базе данных
conn = sqlite3.connect("Master_pol.db")
cursor = conn.cursor()

# Создание таблиц (если они не существуют)
cursor.execute("""
CREATE TABLE IF NOT EXISTS Material_type (
    ID_Tip_materiala INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Tip_materiala VARCHAR(255) NOT NULL,
    Procent_braka_materiala REAL NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Partner_products (
    INN_ID INTEGER NOT NULL,
    Artikul_ID INTEGER NOT NULL,
    Kolichestvo_produkcii INTEGER NOT NULL,
    Data_prodazhi DATE NOT NULL,
    FOREIGN KEY (INN_ID) REFERENCES Partners(ID_INN),
    FOREIGN KEY (Artikul_ID) REFERENCES Products(ID_Artikul)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Partners (
    ID_INN INTEGER NOT NULL PRIMARY KEY,
    Naimenovanie_partnera VARCHAR(255) NOT NULL,
    Tip_partnera_ID INTEGER NOT NULL,
    Rejting INTEGER NOT NULL,
    Indeks INTEGER NOT NULL,
    Oblast VARCHAR(255) NOT NULL,
    Gorod VARCHAR(255) NOT NULL,
    Ulica VARCHAR(255) NOT NULL,
    Dom VARCHAR(6) NOT NULL,
    Familiya VARCHAR(100) NOT NULL,
    Imya VARCHAR(100) NOT NULL,
    Otchestvo VARCHAR(100) NOT NULL,
    Telefon_partnera VARCHAR(16) NOT NULL,
    Elektronnaya_pochta_partnera VARCHAR(100) NOT NULL,
    FOREIGN KEY (Tip_partnera_ID) REFERENCES Partners_type(ID_Tip_partnera)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Partners_type (
    ID_Tip_partnera INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Tip VARCHAR(255) NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Product_type (
    ID_Tip_produkcii INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Type_produkcii VARCHAR(255) NOT NULL,
    Koefficient_tipa_produkcii REAL NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Products (
    ID_Artikul INTEGER NOT NULL PRIMARY KEY,
    Naimenovanie_produkcii VARCHAR(255) NOT NULL,
    Tip_produkcii_ID INTEGER NOT NULL,
    Minimalnaya_stoimost_dlya_partnera REAL NOT NULL,
    FOREIGN KEY (Tip_produkcii_ID) REFERENCES Product_type(ID_Tip_produkcii)
);
""")

# Вставка тестовых данных
# Типы партнеров
cursor.execute("INSERT INTO Partners_type (Tip) VALUES ('ЗАО');")
cursor.execute("INSERT INTO Partners_type (Tip) VALUES ('ООО');")
cursor.execute("INSERT INTO Partners_type (Tip) VALUES ('ПАО');")
cursor.execute("INSERT INTO Partners_type (Tip) VALUES ('ОАО');")

# Партнеры
cursor.execute("""
INSERT INTO Partners (
    ID_INN, Naimenovanie_partnera, Tip_partnera_ID, Rejting, Indeks, Oblast, Gorod, Ulica, Dom, 
    Familiya, Imya, Otchestvo, Telefon_partnera, Elektronnaya_pochta_partnera
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
""", (1237, "Партнер 1", 1, 10, 143960, "Московская", "Реутов", "Свободы", "51", "Иванов", "Иван", "Иванович", "+7 223 322 22 32", "ivanov@example.com"))

cursor.execute("""
INSERT INTO Partners (
    ID_INN, Naimenovanie_partnera, Tip_partnera_ID, Rejting, Indeks, Oblast, Gorod, Ulica, Dom, 
    Familiya, Imya, Otchestvo, Telefon_partnera, Elektronnaya_pochta_partnera
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
""", (12348, "Партнер 2", 2, 8, 652050, "Кемеровская", "Юрга", "Лесная", "15", "Петров", "Петр", "Петрович", "+7 493 123 45 67", "petrov@example.com"))

# Продукты партнеров
cursor.execute("INSERT INTO Partner_products (INN_ID, Artikul_ID, Kolichestvo_produkcii, Data_prodazhi) VALUES (?, ?, ?, ?);", (1, 101, 15000, "2023-01-01"))
cursor.execute("INSERT INTO Partner_products (INN_ID, Artikul_ID, Kolichestvo_produkcii, Data_prodazhi) VALUES (?, ?, ?, ?);", (2, 102, 12000, "2023-02-01"))

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()
'''
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Мастер пол")
        self.setWindowIcon(QIcon("logo.ico"))
        self.setGeometry(100, 100, 800, 600)

        # Установка шрифта и цвета фона
        font = QFont("Segoe UI", 12)
        self.setFont(font)
        self.setStyleSheet("background-color: #F4E8D3;")

        # Подключение к базе данных должно быть первым шагом
        self.db_connection = None
        self.cursor = None
        self.connect_to_database()

        if not self.db_connection or not self.cursor:
            print("База данных не инициализирована. Завершение работы программы.")
            sys.exit(1)  # Выход из программы, если база данных не подключена

        # Главный макет
        main_layout = QVBoxLayout()

        # Логотип и заголовок
        header_layout = QHBoxLayout()
        logo_label = QLabel()
        pixmap = QPixmap("logo.png").scaled(QSize(100, 100), Qt.KeepAspectRatio)
        logo_label.setPixmap(pixmap)
        title_label = QLabel("Мастер пол")
        title_label.setFont(QFont("Segoe UI", 24, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        header_layout.addWidget(logo_label, alignment=Qt.AlignLeft)
        header_layout.addWidget(title_label, stretch=1, alignment=Qt.AlignCenter)

        # Страницы
        self.stacked_widget = QStackedWidget()
        self.page_partners = PartnersPage(self)  # Передаем ссылку на MainWindow
        self.page_edit = EditPartnerPage(self)
        self.page_add = AddPartnerPage(self)
        self.stacked_widget.addWidget(self.page_partners)
        self.stacked_widget.addWidget(self.page_edit)
        self.stacked_widget.addWidget(self.page_add)

        # Кнопки внизу
        button_layout = QHBoxLayout()
        back_button = QPushButton("Назад")
        back_button.setStyleSheet("background-color: #67BA80;")
        back_button.clicked.connect(self.go_back)
        button_layout.addWidget(back_button, alignment=Qt.AlignLeft)

        # Объединение всех элементов
        main_layout.addLayout(header_layout)
        main_layout.addWidget(self.stacked_widget)
        main_layout.addLayout(button_layout)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def connect_to_database(self):
        try:
            # Создаем соединение с базой данных
            self.db_connection = sqlite3.connect("Master_pol.db")
            if self.db_connection:
                # Создаем курсор
                self.cursor = self.db_connection.cursor()
                print("Подключение к базе данных успешно.")
            else:
                raise sqlite3.Error("Не удалось установить соединение с базой данных.")
        except sqlite3.Error as e:
            print(f"Ошибка подключения к базе данных: {e}")
            QMessageBox.critical(None, "Ошибка", f"Не удалось подключиться к базе данных. Подробности: {e}", QMessageBox.Ok)

    def go_back(self):
        self.stacked_widget.setCurrentWidget(self.page_partners)

    def closeEvent(self, event):
        # Закрываем соединение с базой данных при выходе из программы
        if self.db_connection and isinstance(self.db_connection, sqlite3.Connection):
            self.db_connection.close()
            print("Соединение с базой данных закрыто.")
        event.accept()
    
    def calculate_material_quantity(self, product_type_id, material_type_id, product_count, param1, param2):
        query = """
        SELECT 
            pt.Koefficient_tipa_produkcii, mt.Procent_braka_materiala
        FROM 
            Product_type pt
        JOIN 
            Material_type mt ON pt.ID_Tip_produkcii = ? AND mt.ID_Tip_materiala = ?;
        """
        try:
            self.cursor.execute(query, (product_type_id, material_type_id))
            result = self.cursor.fetchone()
            if not result:
                return -1

            coefficient, defect_rate = result
            required_material = product_count * param1 * param2 * coefficient
            required_material_with_defect = required_material / (1 - defect_rate)
            return int(required_material_with_defect)
        except sqlite3.Error as e:
            print(f"Ошибка при расчете материалов: {e}")
            return -1


class PartnersPage(QWidget):    
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        layout = QVBoxLayout()
        self.list_view = QListWidget()
        self.list_view.setStyleSheet("""
            QListWidget {
                background-color: white;
                outline: 0;
            }
            QListWidget::item {
                border: 1px solid #ddd;
                padding: 14px;  /* Увеличенный padding */
                margin: 5px;
                min-height: 140px;  /* Увеличена минимальная высота */
            }
            QListWidget::item:selected {
                background-color: #f0f0f0;
            }
        """)
        self.list_view.itemClicked.connect(self.on_item_clicked)
        layout.addWidget(self.list_view)
        add_button = QPushButton("Добавить")
        add_button.setStyleSheet("background-color: #67BA80;")
        add_button.clicked.connect(self.add_partner)
        layout.addWidget(add_button)
        self.setLayout(layout)
        self.load_partners()

    def on_item_clicked(self, item):
        selected_inn = item.data(Qt.UserRole)
        if selected_inn:
            self.parent.page_edit.load_partner_data(selected_inn)
            self.parent.stacked_widget.setCurrentWidget(self.parent.page_edit)

    def add_partner(self):
        self.parent.stacked_widget.setCurrentWidget(self.parent.page_add)

    def load_partners(self):
        query = """
        SELECT 
            p.ID_INN, pt.Tip, p.Naimenovanie_partnera, 
            SUM(pp.Kolichestvo_produkcii) AS total_quantity,
            p.Telefon_partnera, p.Rejting,
            p.Familiya, p.Imya, p.Otchestvo
        FROM 
            Partners p
        JOIN 
            Partners_type pt ON p.Tip_partnera_ID = pt.ID_Tip_partnera
        LEFT JOIN 
            Partner_products pp ON p.ID_INN = pp.INN_ID
        GROUP BY 
            p.ID_INN, pt.Tip, p.Naimenovanie_partnera,
            p.Telefon_partnera, p.Rejting,
            p.Familiya, p.Imya, p.Otchestvo;
        """
        try:
            self.parent.cursor.execute(query)
            partners = self.parent.cursor.fetchall()
            if not partners:
                QMessageBox.warning(None, "Предупреждение", "В базе данных отсутствуют партнеры.", QMessageBox.Ok)
                return

            for partner in partners:
                inn, html = self.format_partner_info(partner)
                item = QListWidgetItem()
                label = QLabel()
                label.setText(html)
                label.setContentsMargins(0, 0, 0, 0)
                label.setStyleSheet("background-color: transparent;")
                label.setWordWrap(True)
                label.setTextFormat(Qt.RichText)  # Явно указываем формат
                label.adjustSize()
                item.setSizeHint(QSize(label.width(), label.height() + 20))
                item.setData(Qt.UserRole, inn)
                self.list_view.addItem(item)
                self.list_view.setItemWidget(item, label)
                label.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        except sqlite3.Error as e:
            QMessageBox.critical(None, "Ошибка", f"Не удалось загрузить список партнеров: {e}", QMessageBox.Ok)


    def format_partner_info(self, partner):
        inn = partner[0]
        tip = partner[1]
        name = partner[2]
        total_quantity = partner[3] if partner[3] else 0
        telefon = partner[4].strip() if partner[4] else "Телефон не указан"
        rejting = partner[5]  # Берем напрямую из базы
        discount = self.calculate_discount(total_quantity)
        director = f"{partner[6]} {partner[7]} {partner[8]}".strip() or "Директор не указан"      
        

        html = f"""
        <div style='font-size: 14pt;'>
            <table width='100%'>
                <tr>
                    <td style='width: 70%;'><b>{tip}</b> | {name}</td>
                    <td style='width: 30%; text-align: right;'>
                        <span style='color:#333;'>{discount}%</span>
                    </td>
                </tr>
            </table>
        </div>
        <div style='font-size: 10pt; color:#666; margin-top: 8px; line-height: 1.4;'>
            <div>{director}</div>
            <div>{telefon}</div>
            <div>Рейтинг: {rejting}</div>
            <div></div>      
        </div>
        """
        return inn, html

    def calculate_discount(self, quantity):
        if quantity < 10000:
            return 0
        elif 10000 <= quantity < 50000:
            return 5
        elif 50000 <= quantity < 300000:
            return 10
        else:
            return 15

class PartnerForm(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        layout = QVBoxLayout()
        form_layout = QFormLayout()
        
        # Поля ввода
        self.inn_input = QLineEdit()
        self.name_input = QLineEdit()
        self.type_combo = QComboBox()
        self.rating_spin = QSpinBox()
        self.index_input = QLineEdit()
        self.region_input = QLineEdit()
        self.city_input = QLineEdit()
        self.street_input = QLineEdit()
        self.house_input = QLineEdit()
        self.director_last_name_input = QLineEdit()
        self.director_first_name_input = QLineEdit()
        self.director_middle_name_input = QLineEdit()
        self.phone_input = QLineEdit()
        self.email_input = QLineEdit()
        
        # Метки ошибок
        self.error_labels = {
            'inn': QLabel(""),
            'name': QLabel(""),
            'rating': QLabel(""),
            'index': QLabel(""),
            'phone': QLabel(""),
            'email': QLabel(""),
            'director': QLabel("")
        }
        
        # Настройка стилей ошибок
        for label in self.error_labels.values():
            label.setStyleSheet("color: red; font-size: 10pt;")
            label.hide()
        
        # Форма с полями и метками ошибок
        form_layout.addRow("ИНН:", self.inn_input)
        form_layout.addRow("", self.error_labels['inn'])
        form_layout.addRow("Наименование:", self.name_input)
        form_layout.addRow("", self.error_labels['name'])
        form_layout.addRow("Тип партнера:", self.type_combo)
        form_layout.addRow("Рейтинг:", self.rating_spin)
        form_layout.addRow("", self.error_labels['rating'])
        form_layout.addRow("Индекс:", self.index_input)
        form_layout.addRow("", self.error_labels['index'])
        form_layout.addRow("Область:", self.region_input)
        form_layout.addRow("Город:", self.city_input)
        form_layout.addRow("Улица:", self.street_input)
        form_layout.addRow("Дом:", self.house_input)
        form_layout.addRow("Фамилия директора:", self.director_last_name_input)
        form_layout.addRow("Имя директора:", self.director_first_name_input)
        form_layout.addRow("Отчество директора:", self.director_middle_name_input)
        form_layout.addRow("", self.error_labels['director'])
        form_layout.addRow("Телефон:", self.phone_input)
        form_layout.addRow("", self.error_labels['phone'])
        form_layout.addRow("Email:", self.email_input)
        form_layout.addRow("", self.error_labels['email'])
        
        layout.addLayout(form_layout)
        self.setLayout(layout)
        
        # Загрузка типов партнеров
        self.load_types()
    
    def load_types(self):
        query = "SELECT ID_Tip_partnera, Tip FROM Partners_type;"
        try:
            self.parent.cursor.execute(query)
            types = self.parent.cursor.fetchall()
            for type_id, type_name in types:
                self.type_combo.addItem(type_name, type_id)
        except sqlite3.Error as e:
            print(f"Ошибка при загрузке типов партнеров: {e}")
    
    def validate_input(self):
        valid = True
        
        # Валидация ИНН
        inn = self.inn_input.text()
        if not inn.isdigit() or len(inn) != 12:
            self.error_labels['inn'].setText("ИНН должен содержать ровно 12 цифр")
            self.error_labels['inn'].show()
            valid = False
        else:
            self.error_labels['inn'].hide()
            
        # Валидация наименования
        name = self.name_input.text().strip()
        if not name:
            self.error_labels['name'].setText("Наименование не может быть пустым")
            self.error_labels['name'].show()
            valid = False
        else:
            self.error_labels['name'].hide()
            
        # Валидация рейтинга
        rating = self.rating_spin.value()
        if not (0 <= rating <= 10):
            self.error_labels['rating'].setText("Рейтинг должен быть от 0 до 10")
            self.error_labels['rating'].show()
            valid = False
        else:
            self.error_labels['rating'].hide()
            
        # Валидация индекса
        index = self.index_input.text()
        if not index.isdigit() or len(index) != 6:
            self.error_labels['index'].setText("Индекс должен содержать 6 цифр")
            self.error_labels['index'].show()
            valid = False
        else:
            self.error_labels['index'].hide()
            
        # Валидация телефона
        phone = self.phone_input.text()
        if not re.match(r'^\+7 \d{3} \d{3} \d{2} \d{2}$', phone):
            self.error_labels['phone'].setText("Формат: +7 XXX XXX XX XX")
            self.error_labels['phone'].show()
            valid = False
        else:
            self.error_labels['phone'].hide()
            
        # Валидация email
        email = self.email_input.text()
        if not re.match(r'.+@.+\..+', email):
            self.error_labels['email'].setText("Неверный формат email")
            self.error_labels['email'].show()
            valid = False
        else:
            self.error_labels['email'].hide()
            
        # Валидация ФИО директора
        director_fields = [
            self.director_last_name_input.text().strip(),
            self.director_first_name_input.text().strip(),
            self.director_middle_name_input.text().strip()
        ]
        if not all(director_fields):
            self.error_labels['director'].setText("Заполните ФИО директора полностью")
            self.error_labels['director'].show()
            valid = False
        else:
            self.error_labels['director'].hide()
            
        return valid

class AddPartnerPage(PartnerForm):
    def __init__(self, parent):
        super().__init__(parent)
        button_layout = QHBoxLayout()
        add_button = QPushButton("Добавить")
        add_button.setStyleSheet("background-color: #67BA80;")
        add_button.clicked.connect(self.add_partner)
        button_layout.addWidget(add_button)
        self.layout().addLayout(button_layout)
    
    def add_partner(self):
        # Сброс ошибок
        for label in self.error_labels.values():
            label.hide()
            
        if not self.validate_input():
            QMessageBox.warning(self, "Ошибка", "Проверьте правильность заполнения полей", QMessageBox.Ok)
            return
            
        # Собираем все данные из полей
        inn = self.inn_input.text()
        name = self.name_input.text()
        type_id = self.type_combo.currentData()
        rating = self.rating_spin.value()
        index = self.index_input.text()
        region = self.region_input.text()
        city = self.city_input.text()
        street = self.street_input.text()
        house = self.house_input.text()
        last_name = self.director_last_name_input.text()
        first_name = self.director_first_name_input.text()
        middle_name = self.director_middle_name_input.text()
        phone = self.phone_input.text()
        email = self.email_input.text()
        
        query = """
        INSERT INTO Partners (
            ID_INN, Naimenovanie_partnera, Tip_partnera_ID, Rejting, Indeks, 
            Oblast, Gorod, Ulica, Dom, Familiya, Imya, Otchestvo, 
            Telefon_partnera, Elektronnaya_pochta_partnera
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """
        try:
            self.parent.cursor.execute(query, (
                inn, name, type_id, rating, index, region, city, 
                street, house, last_name, first_name, middle_name, 
                phone, email
            ))
            self.parent.db_connection.commit()
            QMessageBox.information(None, "Успешно", "Партнер успешно добавлен.", QMessageBox.Ok)
            self.parent.page_partners.list_view.clear()
            self.parent.page_partners.load_partners()
            self.parent.stacked_widget.setCurrentWidget(self.parent.page_partners)
        except sqlite3.Error as e:
            print(f"Ошибка при добавлении партнера: {e}")
            QMessageBox.critical(None, "Ошибка", f"Не удалось добавить партнера. Подробности: {e}", QMessageBox.Ok)

class EditPartnerPage(PartnerForm):
    def __init__(self, parent):
        super().__init__(parent)
        self.inn = None
        button_layout = QHBoxLayout()
        save_button = QPushButton("Сохранить")
        save_button.setStyleSheet("background-color: #67BA80;")
        save_button.clicked.connect(self.save_partner)
        history_button = QPushButton("История реализации")
        history_button.setStyleSheet("background-color: #67BA80;")
        history_button.clicked.connect(self.show_sales_history)
        button_layout.addWidget(save_button)
        button_layout.addWidget(history_button)
        self.layout().addLayout(button_layout)
    
    def load_partner_data(self, inn):
        query = """
        SELECT 
            ID_INN, Naimenovanie_partnera, Tip_partnera_ID, Rejting, Telefon_partnera, 
            Elektronnaya_pochta_partnera, Indeks, Oblast, Gorod, Ulica, Dom, 
            Familiya, Imya, Otchestvo
        FROM 
            Partners
        WHERE ID_INN = ?;
        """
        try:
            self.parent.cursor.execute(query, (inn,))
            partner = self.parent.cursor.fetchone()
            if partner:
                self.inn = partner[0]
                self.inn_input.setText(str(partner[0]))
                self.name_input.setText(partner[1])
                self.type_combo.setCurrentIndex(partner[2] - 1)
                self.rating_spin.setValue(partner[3])
                self.phone_input.setText(partner[4])
                self.email_input.setText(partner[5])
                
                # Заполнение адресных полей
                self.index_input.setText(str(partner[6]))  # Индекс
                self.region_input.setText(partner[7])      # Область
                self.city_input.setText(partner[8])       # Город
                self.street_input.setText(partner[9])     # Улица
                self.house_input.setText(partner[10])     # Дом
                
                # Заполнение ФИО директора
                self.director_last_name_input.setText(partner[11])
                self.director_first_name_input.setText(partner[12])
                self.director_middle_name_input.setText(partner[13])
        except sqlite3.Error as e:
            print(f"Ошибка при загрузке данных партнера: {e}")
    
    def save_partner(self):
        # Сброс ошибок
        for label in self.error_labels.values():
            label.hide()
            
        if not self.validate_input():
            QMessageBox.warning(self, "Ошибка", "Проверьте правильность заполнения полей", QMessageBox.Ok)
            return
            
        # Собираем все данные из полей
        inn = self.inn_input.text()
        name = self.name_input.text()
        type_id = self.type_combo.currentData()
        rating = self.rating_spin.value()
        index = self.index_input.text()
        region = self.region_input.text()
        city = self.city_input.text()
        street = self.street_input.text()
        house = self.house_input.text()
        last_name = self.director_last_name_input.text()
        first_name = self.director_first_name_input.text()
        middle_name = self.director_middle_name_input.text()
        phone = self.phone_input.text()
        email = self.email_input.text()
        
        query = """
        UPDATE Partners
        SET 
            Naimenovanie_partnera = ?, 
            Tip_partnera_ID = ?, 
            Rejting = ?, 
            Telefon_partnera = ?, 
            Elektronnaya_pochta_partnera = ?,
            Indeks = ?, 
            Oblast = ?, 
            Gorod = ?, 
            Ulica = ?, 
            Dom = ?,
            Familiya = ?, 
            Imya = ?, 
            Otchestvo = ?
        WHERE ID_INN = ?;
        """
        try:
            self.parent.cursor.execute(query, (
                name, type_id, rating, phone, email,
                index, region, city, street, house,
                last_name, first_name, middle_name,
                inn
            ))
            self.parent.db_connection.commit()
            QMessageBox.information(None, "Успешно", "Данные партнера обновлены.", QMessageBox.Ok)
            self.parent.page_partners.list_view.clear()
            self.parent.page_partners.load_partners()
            self.parent.stacked_widget.setCurrentWidget(self.parent.page_partners)
        except sqlite3.Error as e:
            print(f"Ошибка при сохранении партнера: {e}")
            QMessageBox.critical(None, "Ошибка", f"Не удалось сохранить данные партнера. Подробности: {e}", QMessageBox.Ok)
    
    def show_sales_history(self):
        if not self.inn:
            QMessageBox.warning(None, "Предупреждение", "Выберите партнера для просмотра истории.", QMessageBox.Ok)
            return
        
        # Создаем новую страницу для истории продаж
        sales_history_page = SalesHistoryPage(self.parent, self.inn)  # Создаем экземпляр класса
        self.parent.stacked_widget.addWidget(sales_history_page)  # Добавляем страницу в стек
        self.parent.stacked_widget.setCurrentWidget(sales_history_page)  # Переключаемся на новую страницу

        


class SalesHistoryPage(QWidget):
    def __init__(self, parent, partner_inn):
        super().__init__()
        self.parent = parent
        self.partner_inn = partner_inn

        layout = QVBoxLayout()

        # Создаем таблицу
        self.table_widget = QTableWidget()  # Используем QTableWidget
        self.table_widget.setColumnCount(3)  # Три столбца: Наименование продукции, Количество, Дата
        self.table_widget.setHorizontalHeaderLabels(["Продукт", "Количество", "Дата"])
        self.table_widget.setStyleSheet("background-color: white;")

        # Настройка растягивания столбцов
        horizontal_header = self.table_widget.horizontalHeader()
        horizontal_header.setSectionResizeMode(QHeaderView.Stretch)  # Растягиваем столбцы
        horizontal_header.setStretchLastSection(True)  # Убеждаемся, что последний столбец растянут

        layout.addWidget(self.table_widget)

        # Кнопка "Назад"
        button_layout = QHBoxLayout()
        back_button = QPushButton("Назад")
        back_button.setStyleSheet("background-color: #67BA80;")
        back_button.clicked.connect(self.go_back)
        button_layout.addWidget(back_button)

        layout.addLayout(button_layout)
        self.setLayout(layout)

        # Загрузка истории продаж
        self.load_sales_history()

    def load_sales_history(self):
        query = """
        SELECT 
            p.Naimenovanie_produkcii, pp.Kolichestvo_produkcii, pp.Data_prodazhi
        FROM 
            Partner_products pp
        JOIN 
            Products p ON pp.Artikul_ID = p.ID_Artikul
        WHERE 
            pp.INN_ID = ?;
        """
        try:
            print(self.partner_inn)
            self.parent.cursor.execute(query, (self.partner_inn,))
            sales = self.parent.cursor.fetchall()

            if not sales:
                QMessageBox.information(None, "История реализации", "У партнера нет истории продаж.", QMessageBox.Ok)
                return

            # Очищаем таблицу и добавляем данные
            self.table_widget.setRowCount(len(sales))
            for row, sale in enumerate(sales):
                product_name, quantity, date = sale
                self.table_widget.setItem(row, 0, QTableWidgetItem(product_name))  # Используем QTableWidgetItem
                self.table_widget.setItem(row, 1, QTableWidgetItem(str(quantity)))
                self.table_widget.setItem(row, 2, QTableWidgetItem(str(date)))

        except sqlite3.Error as e:
            print(f"Ошибка при загрузке истории продаж: {e}")
            QMessageBox.critical(None, "Ошибка", f"Не удалось загрузить историю продаж. Подробности: {e}", QMessageBox.Ok)

    def go_back(self):
        self.parent.stacked_widget.setCurrentWidget(self.parent.page_partners)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())