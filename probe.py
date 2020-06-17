import csv          
import pandas as pd
import sys


datos = pd.read_csv('Files\input.csv', header = 0)            # File csv
datos
print(datos)
id1 = datos['id']           # Get data about ID
name = datos['Name']           # Get data about ID
address = datos['Full_Address']
print(id1)
print(name)
print(address)

datos.to_csv('Files\output.csv',columns = ['Name','Full_Address'])

archivo = open("Files\output.csv")
reader = csv.reader(archivo,delimiter=',')
for linea in reader:
    print(linea[0]+"\t" +linea[1]+"\t"+linea[2])