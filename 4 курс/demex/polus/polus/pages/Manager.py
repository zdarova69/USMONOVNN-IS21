from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (    
    QDialog # это базовый класс диалогового окна
)

class Manager(QDialog):
    def __init__(self):        
        super(Manager, self).__init__()
        print("Проверка открытия страницы менеджера")