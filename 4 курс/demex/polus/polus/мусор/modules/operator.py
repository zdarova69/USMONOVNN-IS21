from PyQt5.QtWidgets import (    
    QDialog # это базовый класс диалогового окна
)

class operator(QDialog):
    def __init__(self):        
        super(operator, self).__init__()
        print("operator")