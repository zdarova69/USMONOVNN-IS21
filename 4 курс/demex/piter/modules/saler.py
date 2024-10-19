from PyQt5.QtWidgets import (    
    QDialog # это базовый класс диалогового окна
)

class saler(QDialog):
    def __init__(self):        
        super(saler, self).__init__()
        print("saler")