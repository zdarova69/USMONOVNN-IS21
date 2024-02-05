15.01.2023
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
4. Удаление
Обычный файл (regural):
1. touch main.txt
2. mv home/stud/'ваш путь'

