o 15.01.2023
git bash - команды для работы с гит из терминала
Прокси сервер git config --global http.proxy 10.0.50.52:3128
практические задания - https://smartiqa.ru/courses/git/answer-key ![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/fd58582d-0161-4b54-befb-95ce71181d20)

Создание репозитория на компьютере: инициализация git init

$ git status - показывает статус репозитория
On branch master - указывает имя ветки

No commits yet - нет комитов

Untracked files: - неотслеживаемые файлы
  (use "git add <file>..." to include in what will be committed) - нужна команда добавить чтобы зафиксировать версию для сохранения
        index.html - список файлов на сохранение
        pictures/

nothing added to commit but untracked files present (use "git add" to track) - найдены файлы для добавление

п 2. Настраиваем пользователя Git

# Задаем имя и email пользователя для текущего репозитория 23-12 303-15
$ git config  - - global user.name PK303-0 
$ git config  - - global user.email PK303-0@gmail.com

# отмена прокси
git config --global –unset http.proxy
git config --global --unset https.proxy
git config --global --unset core.gitproxy

# добавление файлов  
![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/385d6375-52c9-47aa-b698-d201c53a7520)

# Делаем коммит
$ git commit -m "G-02: Fixed typo in Elephant"

Для фиксации версии нужно указать ее название. Для этого создается сообщение. Оно может быть на русском
# вывод информации
$ git log
![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/e3659ec2-5b2d-47e0-9ecf-fa24bf7997e7)

# Подтверждение гит
![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/99532c7e-6a9a-49d6-a7a9-7f65140802dc)
![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/d5f0bdca-73d7-4a4d-817e-2ba7a5bb75b2)

# пушим гит
![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/d79f8718-8236-4a6a-b3c2-830ca98cc0dc)

основные ошибки: 
1. git remote - подключение к удаленному репозиторию(показывает,на какой репозиторий мы хотим сохранить данные). Может быть ошибка,что неправильно указали ссылку. Чтобы изменить,добавить set-url
2. Авторизация - гитхабу нужно передать данные пользователя(логин,пароль или токен)
3. Прокси сервер - проверять,включен или нет   
#  дебиан C
![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/8ff03405-2f10-4316-b137-e6bf47d42c7f)

# редос python
![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/0ba364fe-c25e-45c6-875d-7bca84c7c7cf)

# ЛК 05.02 РАБОТА С ФАЙЛАМИ

1. Создание
2. Перемещение
3. Редактирование
4. чтение
5. Удаление
   
Обычный файл (regural):

1. touch main.txt - создание
2. mv home/stud/'ваш путь' - перемещение
3. nano main.txt - редактирование
4. cat main.txt - чтение
5. rm main.txt - удаление
   
![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/3f67c33b-fbc1-4e8d-b7d2-af214f65a2d1)
![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/176e17a4-3cc1-4ddb-b150-94486d2db513)

папка (директория):

1. mkdir main - создание
2. mv home/stud/'ваш путь' - перемещение
3. rm main -r - удаление
4. ls main - чтение

![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/a633bce2-491b-4696-bea2-5b245ca9793a)
![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/ee30b7d9-b3fc-4c1f-b395-1cd95e58bdbd)


# ссылки
ln -s main.txt smain.txt - мягкая ссылка
ln main.txt hmain.txt
![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/7c3e6057-22f5-4a83-9802-90e2511de7cb)
![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/6ee2eeef-22ef-4c45-8787-4c65296e5ad9)

![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/9f86764e-4404-4dc2-a0b6-f848d7a10aae)

# Передача данных:сокеты(soket) и каналы(pipe)

Разница в способе передачи данных

fifo - first in first out
![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/0868088e-520f-44b8-9122-8ac132eca1b1)
![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/e0a44d1e-2c79-4aaf-9191-31ced7212df3)
![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/307cff66-90a6-41ab-a375-5582653ff99b)
![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/95e78334-e44d-45b7-bb15-c83ae02aac18)

mcfifo pkanal

![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/aaf20cce-b25b-496b-a690-4397646ae935)


![изображение](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/26f9d16e-232b-4b4e-bba7-c1a6a511a928)
![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/48f6e0f3-a38c-4bfb-9b98-99be307194cd)

# ЛК 3 12.02
Устройства:
1. символьные (мышка,клавиатура)
2. Блочные (флешки)

Файлам присваивается уникальный номер - enod, посмотреть командой ls i1. Жёсткие ссылки имеют тот же номер, что и исходный файл и это можно использовать чтобы найти все жёсткие ссылки.

1.mknod - создание блочного файла
![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/b7a88916-0496-4cb7-b916-6c04b6d931f6)

![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/bee11ece-57b5-47b1-b9ee-7a1301522af5)

![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/bbb0752f-c27b-4f31-9a43-91f28ca52735)

Скрипты

![image](https://github.com/SERGEo10/6semestr/assets/106819250/d8199296-0d5d-4c76-821e-7b9852fbe802)

![image](https://github.com/SERGEo10/6semestr/assets/106819250/18e6046d-fffb-474d-922a-5c3e65ea1e20)

![image](https://github.com/SERGEo10/6semestr/assets/106819250/ec873e9a-2335-47ef-bd16-29b374ff4773)

тот самый скрипт
![Screenshot_1](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/bdbb45ee-8926-466a-8ee7-dd292184dc3d)
![Screenshot_4](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/7079e005-0a24-4f7b-bbcb-0f56d61d4b97)
![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/d04727c8-89ea-4886-831d-96cf96987606)

# ЛК 3 19.02 пользователи
![Screenshot_6](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/0d36d161-69f7-4746-9411-82f66dbef9d8)

stud - имя пользователя
x - пароль
1000 - номер пользователья
1000 - номер группы

bin\bash - терминал пользователя
![Screenshot_7](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/42cb64d3-ebd0-4c80-a4de-43d916aa65e1)
![Screenshot_10](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/511e1003-d4e3-4776-9ef0-9d6c2c7b17b3)
![Screenshot_9](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/6b1fdd6c-3beb-4e2e-b2d4-2545c118ea1c)
![Screenshot_8](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/890431d8-7434-481f-9501-1b627d9642dd)
![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/f1c30152-90e4-4f6f-a1f8-a3ac8c01d3d9)



ред ос
![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/81064b99-d36d-4a02-b63e-0321f98539a3)
![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/b749dcc7-892d-4f46-a82c-bbddf3203be2)

![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/8f056159-ff6d-487e-8bec-e0dfe1b3b9ee)
![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/f2e90696-22ae-488e-8b56-6f6d1c33bd14)

графически:

![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/45dbc310-9c15-4454-b2f7-630d8bfc35f5)

![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/1467bb6e-5240-4410-96a2-bea3fa83a352)


![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/8f744e8f-6ef0-4b33-be69-e23bfc1bfa7f)

![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/63929281-3159-4b8d-b295-7bba8e9fe035)

# ЛК 4 Структура процесса

![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/aeeb513a-8ddc-4e6a-aba5-6d53a8374509)

![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/edd7f8e7-5a80-4da5-b5c1-6973df332514)

![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/a0734a9a-ac89-4dfa-8529-392d6f6f901c)

![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/b7a634a0-fab9-4cf8-906d-1b7564a1e101)

![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/6a1de623-3b1f-42f1-aa23-0b6c4b9fe5b0)

![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/99e3dec5-89a7-4559-9391-822ed04cfccd)

![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/f62329e0-a9a9-439b-8759-17c06acdbc58)

# ЛК 5 11.03 Потоки в БД
Аттрибуты процесса: 
1.PID - уникальный идентификатор 
2.Адресация областей памяти 
3.FD - открытые файловые дескрипторы(терминал или файлы которые используют процессы) 
4.Обработчики сигналов процесса(запросы от пользователей) 
5.Код выходы(ctrl+c, ctrl+z, all done, exit button) 
6.Рабочий каталог(версия ОС)

![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/f6eb6162-e230-4e82-9ef8-38d994df81db)

1 процесс в системе - init

![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/6f8d5c32-f318-4de4-aa6f-31e145d9d78a)

смерть процесса - exit() или kill.

остановка родительского процесса - дочерний переходит в зомби,либо к другому родительскому.
Ready - процесс готов к выполнению,но находится в очереди
Running - запущенный процесс
Если процесс в состоянии Stopped(T) то помочь ему вернуться может SIGCONT)
после ctrl z возобновить может fg

![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/3a56bf6e-3547-44ec-bb51-34e0cb3aa29e)

Терминал
сигнал - способ оповестить процесс о наступлении событий

![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/2d79cd80-61e3-46d2-a1a2-37d4ec831913)

Прерывание - аппаратные и программные.

![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/5463ae02-0aaa-4cbf-80ae-043279fa025a)

Прервывания

Аппаратные и программные. К аппаратным относиться клавиатура, мышка и т.д. К программным всё что с кодом и т.д.

Планировщик процессов

Вытесняющая и кооперативная многозадачность. Кооперативная - программа сама решает когда нужно прекратить выполнение. Вытесняющая решение о переключение на другой процесс принимает сам планировщик.

Debian

Запуск и проверка состояния сервера

![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/02bc1295-4e14-4236-b784-9bb29af8d254)
![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/5e9ab8c7-6070-4165-a0f4-db04452e1aa1)

Переход в работу с базой данных

![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/d6f64446-3310-4691-ab10-c1b54af7f5ab)

Создание и изменение данных в таблице

![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/8539b568-a207-4f1c-b54c-174d497f2b29)
![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/2352ea00-230e-406a-82f4-fd45192b8ed3)

Структура БД

![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/7f6dfe0a-8546-494c-8729-a2ce87004cb0)

Проверяем количество строк
![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/5058d3ef-b504-4453-8eeb-51ffb01e724c)

Далее создадим класс Cursor, при инициализации которого вызывается блокировка потока, обнуляется позиция и передается количество строк в базе. Для потоко-безопасного получения следующего индекса напишем функцию next, которая смещает счетчик позиции на 1, пока мы не пройдем по всем строкам базы. Чтобы пользователь видел, на каком шаге программа, будем выводить в консоль на какой мы позицию с шагом в 10.000. Пример вывода на экран на скриншоте:

![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/1f7afc8e-52c5-4e7b-b19e-3af1955d9511)
![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/d7557f7f-a043-4cc5-8495-b7d7d1722321)
![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/7ed0414e-a6fa-4b03-b1ac-5885b2cb370b)
![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/9d1d3cd2-242c-4af3-983b-db39b57dbc93)

Подключаемся для каждого потока к нашей БД, определяем нашу позицию с помощью класса Cursor и создадим файл для записи с именем res_Номер потока_False, где False означает, что вначале рассматривается использование буфера. Когда мы не используем буфер, строки сначала записываются во все 10 файлов, потом 11 снова записывается в первый файл. Функция flush очищает выходной буфер и перемещает буферизованные данные на диск. Мы создали условие if flush: (чтобы использовать ее только во 2м случае, когда передадим параметр True). В этом случае сначала все строки записываются в 0й файл, потом переходят к 1му и так далее. Файл True.

# ЛК 6. Брокеры сообщений и докер
RabbitMQ - брокер сообщений с открытым исходным кодом. Брокер - инструмент для передачи данных

![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/c6098d6b-7048-4bd1-b11f-33a4deb876ae)
У нас есть издатель и потребитель. Сообщения хранятся в очереди(queues). Обмен(Exchange) и распределение между очередями(binding).
Docker - ПО с открытым кодом, позволяет переносить программные продукты. Может съедать много памяти.

![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/d3cbf4ca-e09c-49cb-89fc-4a624ef9d116)
Клиент - интерфейс. Демон - управление объектами докера. Контейнер - программа. Образ - конфигурация в файле.

#  Задание 6
  
![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/92006ac0-3b19-4fe1-94c6-3af33bad982f)
![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/2a211e36-21a0-4c42-959a-477906b3b79f)
![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/e396ad4c-7a0e-4555-a042-da59cb6ecf82)

![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/6981886b-6dce-4f1d-a119-b0b0322b8008)


![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/ec4bcb03-a291-461b-b1a5-849e68a20cff)
![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/85507324-8bfe-4624-8aac-3f28b4f7efcd)

# Задание 7
установка

    # influxdata-archive_compat.key GPG Fingerprint: 9D539D90D3328DC7D6C8D3B9D8FF8E1F7DF8B07E
    wget -q https://repos.influxdata.com/influxdata-archive_compat.key
    echo '393e8779c89ac8d958f81f942f9ad7fb82a25e133faddaf92e15b16e6ac9ce4c influxdata-archive_compat.key' | sha256sum -c && cat influxdata-archive_compat.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/influxdata-archive_compat.gpg > /dev/null
    echo 'deb [signed-by=/etc/apt/trusted.gpg.d/influxdata-archive_compat.gpg] https://repos.influxdata.com/debian stable main' | sudo tee /etc/apt/sources.list.d/influxdata.list

    sudo apt-get update && sudo apt-get install influxdb
    sudo service influxdb start

    sudo apt-get update && sudo apt-get install influxdb
    sudo systemctl unmask influxdb.service
    sudo systemctl start influxdb

    curl -s https://repos.influxdata.com/influxdata-archive_compat.key | gpg --import

    wget https://dl.influxdata.com/influxdb/releases/influxdb-1.8.10_linux_amd64.tar.gz.asc

    gpg --verify influxdb-1.8.10_linux_amd64.tar.gz.asc influxdb-1.8.10_linux_amd64.tar.gz
![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/bb85f888-35d5-43eb-abca-341398e6d42b)

![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/81925fb8-ee80-4f0b-8f2e-6835d464e5bd)

    wget https://dl.influxdata.com/influxdb/releases/influxdb-1.7.6.x86_64.rpm
    
    sha256sum influxdb-1.7.6.x86_64.rpm
    
    dnf localinstall influxdb-1.7.6.x86_64.rpm 
    
    cat > /etc/yum.repos.d/influxdb.repo << EOF
    [influxdb]
    name = InfluxDB Repository
    baseurl = https://repos.influxdata.com/rhel/7Server/x86_64/stable/
    enabled = 1
    gpgcheck = 1
    gpgkey = https://repos.influxdata.com/influxdb.key
    EOF
    
    dnf update
    dnf install influxdb 
    
    systemctl start influxdb
    systemctl enable influxdb
    
    firewall-cmd --add-port={8086,8088}/tcp --permanent
    firewall-cmd --reload
    
    curl -XPOST "http://localhost:8086/query" --data-urlencode "q=CREATE DATABASE testdb"

  ![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/7f443597-e37d-4cca-8887-836d0f96f1ef)
