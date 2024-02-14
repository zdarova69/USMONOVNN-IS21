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

# Передача данных:сокеты(soket) и каналы(pipe)

Разница в способе передачи данных

fifo - first in first out
![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/0868088e-520f-44b8-9122-8ac132eca1b1)
![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/e0a44d1e-2c79-4aaf-9191-31ced7212df3)
![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/307cff66-90a6-41ab-a375-5582653ff99b)

mcfifo pkanal

![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/aaf20cce-b25b-496b-a690-4397646ae935)

# ЛК 3 12.02
Устройства:
1. символьные (мышка,клавиатура)
2. Блочные (флешки)

1.mknod - создание блочного файла
![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/b7a88916-0496-4cb7-b916-6c04b6d931f6)

![image](https://github.com/zdarova69/USMONOVNN-IS21/assets/113101818/bee11ece-57b5-47b1-b9ee-7a1301522af5)


