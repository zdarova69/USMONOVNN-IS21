from PyQt5.QtWidgets import (    
    QDialog # это базовый класс диалогового окна
)

class zakazchik(QDialog):
    def __init__(self):        
        super(zakazchik, self).__init__()
        print("zakazchik")