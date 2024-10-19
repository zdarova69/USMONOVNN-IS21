from PyQt5.QtWidgets import (    
    QDialog # это базовый класс диалогового окна
)

class admin(QDialog):
    def __init__(self):        
        super(admin, self).__init__()
        print("admin")