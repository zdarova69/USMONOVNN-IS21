import uuid
import json
from yookassa import Configuration, Payment
from ukassa import account_id, secret_key, proxy_api
import sqlite3
from openai import OpenAI
from payments import payment

    
Configuration.account_id = account_id
Configuration.secret_key = secret_key

class Client():
    def __init__(self,):
        # self.tgID = tgID
        # self.name = name
        # self.date_start = date_start
        # self.model = model
        self.db = 'db.db'
        self.model_list = {
            'OpenAI GPT-4.0':{
                "model":'gpt-4o-mini',
                'base_url': "https://api.proxyapi.ru/openai/v1"
            },
            'OpenAI o1':{
                "model":'o1-mini',
                'base_url': "https://api.proxyapi.ru/openai/v1"
            },
            'Google Gemini':{
                "model":'gemini-1.5-flash',
                'base_url': "https://api.proxyapi.ru/google/v1"
            }            
        }
    def new_user(self,  tgID, name, date_start, model = "Gigachat"):
        conn = sqlite3.connect(self.db)
        cursor = conn.cursor()
        # Вставка данных в таблицу users
        cursor.execute('''
        INSERT OR IGNORE INTO users (tgID, name, date_start, model)
        VALUES (?, ?, ?, ?)
        ''', (tgID, name, date_start, model))
        print('данные сохранены')
        conn.commit()
    def check_status(self, tgID, description):
        conn = sqlite3.connect(self.db)
        cursor = conn.cursor()
        # Сначала проверяем, существует ли запись с таким tgID и описанием "подписка за телеграмм-бота"
        cursor.execute('''
            SELECT status FROM payments
            WHERE tgID = ? AND description = ?
        ''', (tgID, description))

        status = cursor.fetchone()[0]
        print(status)
        conn.commit()
        conn.close()
    def create_payment(self, tgID, value, description):
            try:           
                status = self.check_status(tgID=tgID, description=description)
                if status and status == 'succesfull':
                    print('подписка уже есть')
                    return 'у вас есть подписка'
                else:
                    # Создаем новый платеж вместо старого
                    payment_check = payment(value=value, description=description)

                    payment_url = payment_check['confirmation']['confirmation_url']

                    # Получаем значения
                    PaymentID = payment_check['id']
                    status = payment_check['status']
                    description = payment_check['description']
                    value = payment_check['amount']['value']
                    created_at = payment_check['created_at']
                    
                    conn = sqlite3.connect(self.db)
                    cursor = conn.cursor()

                    if status:  
                        # Если запись существует, обновляем остальные атрибуты
                        cursor.execute('''
                            UPDATE payments
                            SET PaymentID = ?, status = ?, value = ?, created_at = ?
                            WHERE tgID = ? AND description = 'Подписка на телеграмм-бота'
                        ''', (PaymentID, status, value, created_at, tgID))
                    else:
                        # Если записи не существует, добавляем новую запись
                        cursor.execute('''
                            INSERT INTO payments (PaymentID, status, description, tgID, value, created_at)
                            VALUES (?, ?, ?, ?, ?, ?)
                        ''', (PaymentID, status, description, tgID, value, created_at))

                    conn.commit()
                    conn.close()
            except Exception as e:
                print(f"An error occurred: {e}")
                conn.rollback()
            return payment_url
    
    def change_model(self, tgID, model):
        # Обновляем информацию о пользователе в базе данных
        conn = sqlite3.connect(self.db)
        cursor = conn.cursor()     
        # Проверяем, существует ли пользователь в базе данных
        cursor.execute('SELECT * FROM users WHERE tgID = ?', (tgID,))
        user_exists = cursor.fetchone()
        
        if user_exists:
            # Если пользователь существует, обновляем его запись
            cursor.execute('''
                UPDATE users
                SET model = ?
                WHERE tgID = ?
            ''', (model, tgID))
        else:
            # Если пользователь не существует, добавляем новую запись
            cursor.execute('''
                INSERT INTO users (tgID, model)
                VALUES (?, ?)
            ''', (tgID, model))   
        conn.commit()
        conn.close()

    def generate_text(self, tgID, prompt:str): 
        # Обновляем информацию о пользователе в базе данных
        conn = sqlite3.connect(self.db)
        cursor = conn.cursor()     
        # Проверяем, существует ли пользователь в базе данных
        cursor.execute('SELECT model FROM users WHERE tgID = ?', (tgID,))
        model = cursor.fetchone()[0]


        client = OpenAI(
            api_key = proxy_api, 
            base_url=self.model_list[model]['base_url'],
        )
        model=self.model_list[model]['model']
    
        if model == 'o1-mini':
            completion = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
        # elif model == 'Google Gemini':
        #     completion = client.chat.completions.create(
        #         model=model['model'],
        #         contents=[
        #             {"role": "user", "content": prompt}
        #         ]
        #     )
        else:
            completion = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "ты - чат-бот ассистент"},
                    {"role": "user", "content": prompt}
                ]
            )
        return completion.choices[0].message.content
    
       
