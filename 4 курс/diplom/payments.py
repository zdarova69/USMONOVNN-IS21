import uuid
import json
from yookassa import Configuration, Payment
from ukassa import account_id, secret_key

Configuration.account_id = account_id
Configuration.secret_key = secret_key

def payment(value, description):
    payment = Payment.create({
        "amount": {
            "value": value,
            "currency": "RUB"
        },
        "payment_method_data": {
            "type": "bank_card"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": "https://t.me/NeuralLLM_Bot"
        },
        "capture": True,
        "description": description,  # Добавлена запятая
        "receipt": {
            "customer": {
                "email": "stapkt@gmail.com"
            },
            "items": [
                {
                    "description": description,
                    "quantity": 1,
                    "amount": {
                        "value": value,
                        "currency": "RUB"
                    },
                    "vat_code": 1
                }
            ]
        }
    })  # Добавлена закрывающая скобка
    return json.loads(payment.json())

	
# a = payment('1','Оплата подписки на бота тест')
# print(a)

# payment_method_id = a['payment_method']['id']
# check = Payment.find_one(payment_method_id)
# print(check)