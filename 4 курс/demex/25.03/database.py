import sqlite3

class DatabaseHandler:
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.connect()
        
    def connect(self):
        """Подключение к базе данных и инициализация"""
        try:
            self.conn = sqlite3.connect('Master_pol.db')
            self.cursor = self.conn.cursor()
            
            # Инициализация типов партнеров
            self.cursor.execute("SELECT COUNT(*) FROM Partners_type")
            if self.cursor.fetchone()[0] == 0:
                types = ['ЗАО', 'ООО', 'ПАО', 'ОАО']
                for t in types:
                    self.cursor.execute("INSERT INTO Partners_type (Tip) VALUES (?)", (t,))
                self.conn.commit()
                
        except sqlite3.Error as e:
            raise Exception(f"Ошибка подключения к БД: {str(e)}")

    def get_partner_types(self):
        """Получение списка типов партнеров"""
        try:
            self.cursor.execute("SELECT Tip FROM Partners_type")
            return [row[0] for row in self.cursor.fetchall()]
        except sqlite3.Error as e:
            raise Exception(f"Ошибка получения типов: {str(e)}")

    def get_partners(self):
        """Получение списка всех партнеров"""
        try:
            self.cursor.execute("""
                SELECT p.*, pt.Tip 
                FROM Partners p
                LEFT JOIN Partners_type pt ON p.Tip_partnera_ID = pt.ID_Tip_partnera
                ORDER BY p.Rejting DESC
            """)
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            raise Exception(f"Ошибка загрузки партнеров: {str(e)}")

    def get_partner(self, inn):
        """Получение данных партнера по ИНН"""
        try:
            self.cursor.execute("""
                SELECT p.*, pt.Tip 
                FROM Partners p
                LEFT JOIN Partners_type pt ON p.Tip_partnera_ID = pt.ID_Tip_partnera
                WHERE p.ID_INN = ?
            """, (inn,))
            partner = self.cursor.fetchone()
            
            if not partner:
                return None
                
            return {
                'inn': str(partner[0]) if partner[0] else None,
                'name': str(partner[1]) if partner[1] else None,
                'type': str(partner[14]) if partner[14] else None,
                'rating': int(partner[3]) if partner[3] else 0,
                'index': str(partner[4]) if partner[4] else None,
                'region': str(partner[5]) if partner[5] else None,
                'city': str(partner[6]) if partner[6] else None,
                'street': str(partner[7]) if partner[7] else None,
                'house': str(partner[8]) if partner[8] else None,
                'last_name': str(partner[9]) if partner[9] else None,
                'first_name': str(partner[10]) if partner[10] else None,
                'middle_name': str(partner[11]) if partner[11] else None,
                'phone': str(partner[12]) if partner[12] else None,
                'email': str(partner[13]) if partner[13] else None
            }
        except sqlite3.Error as e:
            raise Exception(f"Ошибка получения партнера: {str(e)}")

    def save_partner(self, data, is_editing=False):
        """Сохранение партнера в БД"""
        try:
            # Получаем ID типа
            self.cursor.execute("""
                SELECT ID_Tip_partnera 
                FROM Partners_type 
                WHERE Tip = ?
            """, (data['type'],))
            type_id = self.cursor.fetchone()[0]

            # Подготовка данных
            partner_data = (
                data['name'],
                type_id,
                data['rating'],
                data['index'],
                data['region'],
                data['city'],
                data['street'],
                data['house'],
                data['last_name'],
                data['first_name'],
                data['middle_name'],
                data['phone'],
                data['email'],
            )

            if is_editing:
                # Обновление записи
                self.cursor.execute("""
                    UPDATE Partners SET
                        Naimenovanie_partnera = ?,
                        Tip_partnera_ID = ?,
                        Rejting = ?,
                        Indeks = ?,
                        Oblast = ?,
                        Gorod = ?,
                        Ulica = ?,
                        Dom = ?,
                        Familiya = ?,
                        Imya = ?,
                        Otchestvo = ?,
                        Telefon_partnera = ?,
                        Elektronnaya_pochta_partnera = ?
                    WHERE ID_INN = ?
                """, partner_data + (data['inn'],))
            else:
                # Новая запись
                self.cursor.execute("""
                    INSERT INTO Partners VALUES (
                        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 
                        ?, ?, ?, ?
                    )
                """, (data['inn'],) + partner_data)
            
            self.conn.commit()
        except sqlite3.IntegrityError:
            raise ValueError("Партнер с таким ИНН уже существует")
        except sqlite3.Error as e:
            raise Exception(f"Ошибка сохранения: {str(e)}")
    def load_sales_history(self, inn):
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
            sales = self.cursor.execute(query, (inn,))

            return sales

        except sqlite3.Error as e:
            print(f"Ошибка при загрузке истории продаж: {e}")
            raise Exception("Ошибка", f"Не удалось загрузить историю продаж. Подробности: {e}")
    def close(self):
        """Закрытие соединения с БД"""
        if self.conn:
            self.conn.close()