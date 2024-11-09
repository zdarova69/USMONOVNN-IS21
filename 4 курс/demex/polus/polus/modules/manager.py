from PyQt5.QtWidgets import (    
    QDialog # это базовый класс диалогового окна
)

class manager(QDialog):
    def __init__(self):        
        super(manager, self).__init__()
        print("manager")

