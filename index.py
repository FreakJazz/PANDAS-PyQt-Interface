import csv          
import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from MainWindow import *


# Application Class
class Application(QMainWindow):
 #Método constructor de la clase
 def __init__(self):
  #QMainWindow Start
  QMainWindow.__init__(self)
  #Charge MainWindow 
  uic.loadUi("MainWindow.ui", self)
  self.setWindowTitle("SUVECI")


if __name__ == "__main__": 
    app = QApplication(sys.argv)        #App Inicialization
    _Application = Application()        #Object Class
    _Application.show()                 #Show Window
    app.exec_()                         #Execute Aplication