import pika # Python client recommended by the RabbitMQ team

# установить соединение с сервером RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# запрашиваем имя очереди у пользователя
queue = input("Введите имя очереди: ")
# создаем очередь сообщений
channel.queue_declare(queue=queue)

# обмен по умолчанию, обозначенный пустой строкой, позволяет точно указать, в какую очередь должно отправляться сообщение (параметр routing_key)
def send_message():
    message = input("Введите сообщение: ")
    channel.basic_publish(exchange='', routing_key=queue, body=message)

message_count = 0
message_limit = 0

# Выводим информацию о сообщении
def info_message(chanel, method, properties, body):
    global message_count
    print("Сообщение получено: ", chanel, "Текст сообщения: ", body)
    message_count += 1
    # Перед выходом из программы нам нужно убедиться, что сетевые буферы были очищены
    # и наше сообщение действительно было доставлено в RabbitMQ.
    # Мы можем сделать это, закрыв соединение.
    if message_count == message_limit:
        channel.stop_consuming()

# Полуение сообщения
def receive_message():
    channel.basic_consume(on_message_callback=info_message, queue=queue, auto_ack=True)
    channel.start_consuming()

operation = input("Введите send, чтобы отправить сообщение, и receive, чтобы получить: ")
if operation == "send":
    print("Сообщение будет отправлено в очередь: ", queue)
    send_message()
if operation == "receive":
    message_limit = int(input("Введите, сколько сообщений вывести: "))
    receive_message()
    
connection.close()
