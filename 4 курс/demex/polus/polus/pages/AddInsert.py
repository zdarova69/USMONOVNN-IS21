#  widget - это имя, присваиваемое компоненту пользовательского интерфейса,
#  с которым пользователь может взаимодействовать 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (    
    QDialog, # это базовый класс диалогового окна
    QTableWidget
)

from PyQt5.uic import loadUi # загрузка интерфейса, созданного в Qt Creator

import sqlite3

# Окно приветствия
class AddRequest(QDialog):
    """
    Это класс окна приветствия.
    """
    def __init__(self, button, lineIDrequest,
                 linestartDate,
                 lineorgTechTypeID,
                 lineorgTechModel,
                 lineproblemDescryption,
                 linerequestStatusID,
                 linecompletionDate,
                 linerepairParts,
                 linemasterID,
                 lineclientID
                 ):
        """
        Это конструктор класса
        """
        super(AddRequest, self).__init__()        
        self.SaveButton = button
        print(self.SaveButton) 

        self.IDrequestField = lineIDrequest
        print(self.IDrequestField)   
        
        self.startDateField = linestartDate
        print(self.startDateField)
        
        self.orgTechTypeIDField = lineorgTechTypeID
        print(self.orgTechTypeIDField)
        
        self.orgTechModelField = lineorgTechModel
        print(self.orgTechModelField)
        
        self.problemDescryptionField = lineproblemDescryption
        print(self.problemDescryptionField)
        
        self.requestStatusIDField = linerequestStatusID
        print(self.requestStatusIDField)
        
        self.completionDateField = linecompletionDate
        print(self.completionDateField)
        
        self.repairPartsField = linerepairParts
        print(self.repairPartsField)
        
        self.masterIDField = linemasterID
        print(self.masterIDField)
        
        self.clientIDField = lineclientID
        print(self.clientIDField)
        self.SaveButton.clicked.connect(self.SaveFunction)        

    def SaveFunction(self):        
        IDrequest = self.IDrequestField.text() 
        print(IDrequest) 

        startDate = self.startDateField.text() 
        print(startDate)

        orgTechTypeID = self.orgTechTypeIDField.text() 
        print(orgTechTypeID)

        orgTechModel = self.orgTechModelField.text() 
        print(orgTechModel)

        problemDescryption = self.problemDescryptionField.text() 
        print(problemDescryption)

        requestStatusID = self.requestStatusIDField.text() 
        print(requestStatusID)

        completionDate = self.completionDateField.text() 
        print(completionDate)

        repairParts = self.repairPartsField.text() 
        print(repairParts)

        masterID = self.masterIDField.text() 
        print(masterID)

        clientID = self.clientIDField.text() 
        print(clientID)

        conn1 = sqlite3.connect("uchet.db")
        cur1 = conn1.cursor()
               
        cur1.execute(f"""INSERT INTO requests (
                        IDrequest, 
                        startDate, 
                        orgTechTypeID, 
                        orgTechModel, 
                        problemDescryption, 
                        requestStatusID, 
                        completionDate, 
                        repairParts, 
                        masterID, 
                        clientID
                    ) VALUES (
                        {IDrequest},        -- IDrequest (INTEGER)
                        "{startDate}",        -- startDate (TEXT)
                        {orgTechTypeID},        -- orgTechTypeID (INTEGER)
                        "{orgTechModel}",        -- orgTechModel (TEXT)
                        "{problemDescryption}",        -- problemDescryption (TEXT)
                        {requestStatusID},        -- requestStatusID (INTEGER)
                        "{completionDate}",        -- completionDate (TEXT)
                        "{repairParts}",        -- repairParts (TEXT)
                        {masterID},        -- masterID (INTEGER)
                        {clientID}         -- clientID (INTEGER)
                    );
                    """)
        print("test")
        conn1.commit()
        conn1.close()