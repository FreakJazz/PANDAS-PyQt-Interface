import csv          
import pandas as pd
import sys


datos = pd.read_csv('Files\input.csv', header = 0)            # File csv
datos
               
id1 = datos['id']           # Get data about ID
name = list(datos['Name']  )         # Get data about ID
address = datos['Full_Address']
print(id1)
print(name)
print(address)
datos = pd.read_csv('Files\output.csv', header = 0)            # File csv
datos
#print(list(datos.columns.values))
dfObj = pd.DataFrame(columns=['Name', 'Given Name', 'Additional Name', 'Family Name', 'Yomi Name', 'Given Name Yomi', 'Additional Name Yomi', 'Family Name Yomi', 'Name Prefix', 'Name Suffix', 'Initials', 'Nickname', 'Short Name', 'Maiden Name', 'Birthday', 'Gender', 'Location', 'Billing Information', 'Directory Server', 'Mileage', 'Occupation', 'Hobby', 'Sensitivity', 'Priority', 'Subject', 'Notes', 'Language', 'Photo', 'Group Membership', 'Phone 1 - Type', 'Phone 1 - Value', 'Address 1 - Type', 'Address 1 - Formatted', 'Address 1 - Street', 'Address 1 - City', 'Address 1 - PO Box', 'Address 1 - Region', 'Address 1 - Postal Code', 'Address 1 - Country', 'Address 1 - Extended Address', 'Organization 1 - Type', 'Organization 1 - Name', 'Organization 1 - Yomi Name', 'Organization 1 - Title', 'Organization 1 - Department', 'Organization 1 - Symbol', 'Organization 1 - Location', 'Organization 1 - Job Description'])
dfObj['Name'] = name
dfObj['Given Name'] = name
dfObj['Additional Name'] = name
dfObj['Family Name'] = name

#dfObj = dfObj.join(pd.DataFrame([name], index=dfObj.index, columns=['Name', 'Given Name', 'Additional Name','Family Name'])) 
dfObj.to_csv('new.csv', sep='\t')
#print(dfObj)

datos.to_csv('Files\output.csv',columns = ['Name','Full_Address'])

archivo = open("Files\output.csv")
reader = csv.reader(archivo,delimiter=',')
for linea in reader:
    print(linea[0]+"\t" +linea[1]+"\t"+linea[2])