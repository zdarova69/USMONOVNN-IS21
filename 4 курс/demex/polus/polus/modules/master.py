from PyQt5.QtWidgets import (    
    QDialog # это базовый класс диалогового окна
)

class master(QDialog):
    def __init__(self):        
        super(master, self).__init__()
        print("master")
