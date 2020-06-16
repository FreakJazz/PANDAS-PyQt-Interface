import csv          
import pandas as pd
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog
from PyQt5 import uic, QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from MainWindow import *
import ctypes #GetSystemMetrics


# Application Class
class Application(QMainWindow):
    #Método constructor de la clase
    def __init__(self, parent = None):
        #QMainWindow Start
        
        QMainWindow.__init__(self,parent)
        #Charge MainWindow 
        uic.loadUi("MainWindow.ui", self)
        self.setWindowTitle("SUVECI")

        #Agree new item
        self.list_options.addItem("File 3")
        self.list_options.addItem("File 4")
        self.btn_charge.clicked.connect(self.getItem)
    #Eliminar un item
    #self.lenguajes.removeItem(0)
    
    def getItem(self):
        item = self.list_options.currentText()
        self.label_file.setText("Your File have been Charged: " + item)
        df = pd.read_csv('Files\echogar.csv')            # File csv
        print(df)


if __name__ == "__main__": 
    app = QApplication(sys.argv)        #App Inicialization
    _Application = Application()        #Object Class
    _Application.show()                 #Show Window
    app.exec_()                         #Execute Aplication
    #sys.exit(app.exec_())