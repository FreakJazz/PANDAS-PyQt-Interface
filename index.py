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
        self.count = 1
        #Agree new item
        self.list_options.addItem("input.csv")
        self.list_options.addItem("echogar.csv")
        self.list_options.addItem("echogar1.csv")
        self.list_options.addItem("echogar2.csv")
        self.btn_charge.clicked.connect(self.getfile)
        self.btn_process.clicked.connect(self.processfile)
    #Eliminar un item
    #self.lenguajes.removeItem(0)
    
    def getfile(self):
        inputPath = sys.argv[1]
        data = pd.read_csv(inputPath, parse_data = ['Time'])            # File csv
        item = self.list_options.currentText()
        self.label_file.setText("Your File have been Charged: " + item)
        #self.listView.setText(item,self.count)
        self.listWidget.addItem(item)
        self.count +=1
        print(self.count)

    def processfile(self):
        data = pd.read_csv('Files\input.csv')            # File csv
        data_output = pd.read_csv('Files\output.csv')
        print(data)
        print(data_output)
        id1 = data['id']           # Get data about ID
        name = data['Name']           # Get data about ID
        address = data['Full_Address']
        pd.merge(data_output, data, how = 'left', on = name)
        for i  in range(101):
            self.process_bar.setValue(i)
            self.label_process.setText("Processing...")
        self.label_process.setText("Process Finished")
        self.process_bar.setValue(0)
        print(data_output)
        print(data)
        data_output.to_csv('Files\output.csv')

if __name__ == "__main__": 
    app = QApplication(sys.argv)        #App Inicialization
    _Application = Application()        #Object Class
    _Application.show()                 #Show Window
    app.exec_()                         #Execute Aplication
    #sys.exit(app.exec_())