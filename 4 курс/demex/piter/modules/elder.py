from PyQt5.QtWidgets import (    
    QDialog # это базовый класс диалогового окна
)

class elder(QDialog):
    def __init__(self):        
        super(elder, self).__init__()
        print("elders")