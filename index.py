import csv          
import pandas as pd
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog, QFileDialog
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
        self.btn_charge.clicked.connect(self.getfile)
        self.btn_process.clicked.connect(self.processfile)
    #Eliminar un item
    #self.lenguajes.removeItem(0)
    
    def getfile(self):
        self.options = QFileDialog.Options()
        #self.options |= QFileDialog.DontUseNativeDialog
        #fileName, _ = QFileDialog.getOpenFileName(self,"Open File", "","All Files (*);;CSV Files (*.csv)", options=options)
        self.fileNames, _ = QFileDialog.getOpenFileNames(self,"Open File", "","CSV Files (*.csv);;All Files (*)", options=self.options)
        #fileNames, _ = QFileDialog.getSaveFileName(self,"Open File","","All Files (*);;CSV Files (*.csv)", options=options)
        if self.fileNames:
            print(self.fileNames)
            self.lenght = len(self.fileNames)-1
            print(self.lenght)
            while self.lenght >= 0:
                print(self.fileNames[self.lenght])
                self.label_file.setText("Your Files have been Charged: " + str(len(self.fileNames)))
                self.listWidget.addItem(self.fileNames[self.lenght])
                #for i in (self.fileNames[self.lenght].reverse()):
                   # if (i == '.' or i == '/'):
                    #    self.count = i
                    #    break
                #print(self.count)
                self.lenght -=1
            

    def processfile(self):
        if self.fileNames:
            self.lenght = len(self.fileNames)-1
            print(self.lenght)
            while self.lenght >= 0:
                print(self.fileNames[self.lenght])
                data = pd.read_csv(self.fileNames[self.lenght])            # File csv
                name = data['Name']           # Get data about Name
                State = data['State']           # Get data about State
                address = data['Phone']         # Get data about Phone
                data.to_csv(self.fileNames[self.lenght]+"output.csv",columns = ['Name','State', 'Phone'])
                self.lenght -=1
                self.listWidget_2.addItem(self.fileNames[self.lenght]+"output.csv")

        for i  in range(101):
            self.process_bar.setValue(i)
            self.label_process.setText("Processing...")
        self.label_process.setText("Process Finished")
        self.process_bar.setValue(0)

if __name__ == "__main__": 
    app = QApplication(sys.argv)        #App Inicialization
    _Application = Application()        #Object Class
    _Application.show()                 #Show Window
    app.exec_()                         #Execute Aplication
    #sys.exit(app.exec_())