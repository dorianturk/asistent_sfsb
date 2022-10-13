# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 11:16:43 2022

@author: zsk
"""
import PySimpleGUI as sg
import pandas as pd
import numpy as np
import csv
import glob
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import os
import datetime
import calendar
from googletrans import Translator

print('Odaberi kolegij (M1/M2):')
kolegij = input()
print('Odabrani kolegij je:', kolegij)
"""
Dio koda koji dkida zadnje prijavljene studente
"""

username = "dturk@unisb.hr"
password = "gtr456tgh"

chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : r"D:\asistent_sfsb\mehanika2"}
chromeOptions.add_experimental_option("prefs",prefs)
#chromeOptions.add_argument("--headless")
chromeOptions.add_argument('--window-size=1920,1080')
chromedriver = r"C:\python_drivers\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chromeOptions)

driver.get("https://www.isvu.hr/nastavnickiportal/hr/prijava")

driver.find_element_by_class_name("linkSamlPrijava").click()
sleep(.5)
driver.find_element_by_id("username").send_keys(username)
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_class_name("login-btn").click()
sleep(.5)
driver.get("https://www.isvu.hr/nastavnickiportal/hr/ispit/ispitnirok")
sleep(.5)

if kolegij == 'M1':
    driver.find_element_by_xpath("//form[@id='form_218728']//a[@title='Dohvati']").click()
elif kolegij == 'M2':
    driver.find_element_by_xpath("//form[@id='form_218750']//a[@title='Dohvati']").click()
else:
    driver.close()

sleep(.5)
#Meha2
driver.find_element_by_xpath("//span[normalize-space()='Excel']").click()

sleep(1)
driver.close()



"""
#Dio koda koji dolazi do tablice grade1.csv
"""
for datoteka in glob.glob('mehanika2/ispisStudentiNaRoku*'):
    print (datoteka)
    
data = pd.read_excel(datoteka, sheet_name=0, header=18, skipfooter=1, index_col=None, usecols='B:G', dtype={'JMBAG': str})

data.insert(loc=0, column='Rbr.', value=np.arange(start=1, stop=len(data)+1, step=1))

data = data.drop(data.columns[1], axis=1)
data = data.drop(data.columns[4], axis=1)

#print(data)

#Priprema za grade1.csv
data_LaTeX = data.rename(columns = {'Rbr.': 'RB'})
data_LaTeX = data_LaTeX.drop(data.columns[range(4,5)], axis=1)
data_LaTeX["Z1"] = np.nan
data_LaTeX["Z2"] = np.nan
data_LaTeX["Z3"] = np.nan
data_LaTeX["Z4"] = np.nan
data_LaTeX["Z5"] = np.nan
#data_LaTeX["UKUPNO"] = np.nan

#print(data_LaTeX)

data_LaTeX.to_csv('grade1.csv', sep=',', index=False)


"""
#Dio koda koji dobiva podatke za gui
"""
headings_data = pd.read_csv('grade1.csv', dtype={'JMBAG': str})
headings_data_list_old = list(headings_data)

#debugging
#print("redova:", len(headings_data))
#print("stupaca:",  len(headings_data.columns))

test=0

x=495+730
y1=len(headings_data)*22+30
y=y1
scrl = False
if y1 >= 800:
    y1 = 800
    scrl = True
    

headings_data_old = headings_data

headings_data = headings_data.drop(headings_data.index[range(len(headings_data))], axis=0)
headings_data = headings_data.drop(headings_data.columns[range(0,4)], axis=1)
headings_list = list(headings_data)

first_four_columns = headings_data_old.drop(headings_data_old.columns[range(4,9)], axis=1)

first_four_columns.to_csv('first_four_columns.csv', sep=',', index=False)

with open('first_four_columns.csv', newline='', encoding = 'UTF-8') as file:
    reader = csv.reader(file, delimiter = ',')
    headings2 = next(reader)
    first_four_columns = []
    for row in reader:
        first_four_columns.append(row[:])


#debugging
#print("\nheadings_data_old:", headings_data_old, sep='\n')
#print("\nheadings_data:", headings_data, sep='\n')
#print("\nheadings:", headings_list, sep='\n')
#print("\nfirst_four_columns:", first_four_columns, sep='\n')


"""
#Dio koda koji obavlja gui
"""
headings = headings_list
header_list = headings2


layout_left = [	
    [sg.Table(values=first_four_columns, headings=header_list, auto_size_columns=False, col_widths=[4,11,15,15], row_height=22, display_row_numbers=False, justification='center', hide_vertical_scroll=True, num_rows=min(len(first_four_columns)+test, len(first_four_columns)+test))]
	]

naslov=[[sg.Text(h, size=(15,0), justification='center', pad=(0,0)) for h in headings]]

layout_right = naslov + [
    [sg.Input(size=(15,0), pad=(0,0)) for col in range(len(headings_data.columns))] for row in range(len(headings_data_old)+test)
                ] 

layout1 = [
    [sg.Col(layout_left, size=(498,y), scrollable=False), sg.Col(layout_right, size=(730,y), scrollable=False)],
    ]

layout = [
    [sg.Text('Datum uvida u ispit:'), sg.InputText(size=(11,0))],
    [sg.Col(layout1, scrollable=scrl, vertical_scroll_only=True, size=(x,y1))],
    [sg.Submit(), sg.Cancel()]
    ]


window = sg.Window('Unos podataka s ispita', layout, font=("Helvetica", 12), resizable=False)
button, values = window.Read()
window.close()

#debugging
#print("\nPritisnut gumb:", button, sep='\n')
#print("\nVrijednosti iz tablice:", values, sep='\n') 

"""
#Obrada nakon guia
"""
d = {}
for key, value in values.items():
    d[key] = value

listA = list(d.values())

#print(listA)

lista_bodova = [listA[x:x+5] for x in range(2, len(listA),5)]
datumuvida = listA[0]
#print (composite_list)

df_2 = pd.DataFrame(first_four_columns, columns=header_list)
novi_df = pd.DataFrame(lista_bodova, columns =['Z1', 'Z2', 'Z3', 'Z4', 'Z5'])


#print(novi_df)
#print(df_2)

df_out = pd.concat([df_2, novi_df], axis=1)
df_out = df_out.replace(r'^\s*$', np.nan, regex=True)

#print(df_out)
df_out.to_csv('grade.csv', sep=',', index=False)

df_out = pd.read_csv('grade.csv', dtype={'JMBAG': str})  

column_list = list(df_out)

column_list.remove('RB')
column_list.remove('JMBAG')
column_list.remove('Ime')
column_list.remove('Prezime')
#column_list.remove('UKUPNO')

df_out["UKUPNO"] = df_out[column_list].sum(axis=1)

#convert to int

df_out['Z1'] = df_out['Z1'].astype('Int64')
df_out['Z2'] = df_out['Z2'].astype('Int64')
df_out['Z3'] = df_out['Z3'].astype('Int64')
df_out['Z4'] = df_out['Z4'].astype('Int64')
df_out['Z5'] = df_out['Z5'].astype('Int64')
df_out['UKUPNO'] = df_out['UKUPNO'].astype('Int64')

df_out.to_csv('grade.csv', sep=',', index=False)

#Spajanje s latexom
def findDay(datumuvida):
    uviddana = datetime.datetime.strptime(datumuvida, '%d.%m.%Y.').weekday()
    return (calendar.day_name[uviddana])

translator = Translator()
danuvida = translator.translate(findDay(datumuvida), dest='hr')

datumispita = pd.read_excel(datoteka, skiprows=7 - 1, usecols="D", nrows=1, header=None, names=["Value"]).iloc[0]["Value"]
kolegijrez1 = pd.read_excel(datoteka, skiprows=5 - 1, usecols="D", nrows=1, header=None, names=["Value"]).iloc[0]["Value"]
kolegijrez = kolegijrez1.split()[0] + " " + kolegijrez1.split()[1]

texdoc = []  # a list of string representing the latex document in python

# read the .tex file, and modify the lines
with open('rezultati.tex', encoding = 'UTF-8') as fin:
    for line in fin:
        texdoc.append(line.replace('datumispita', datumispita).replace('kolegijrez', kolegijrez).replace('datumuvida', datumuvida).replace('danuvida', danuvida.text))
        
# write back the new document
with open('rezultati_objava.tex', 'w', encoding = 'UTF-8') as fout:
    for i in range(len(texdoc)):
        fout.write(texdoc[i])
        
os.system("pdflatex rezultati_objava.tex")


"""
#premjestanje datoteke u old
"""

source = "D:\asistent_sfsb\mehanika2"
destination = "D:\asistent_sfsb\data_old"
files = os.listdir(source)
 
for f in files:
    os.replace(source + f, destination + f)

"""
#Ideje:
#edit samo file rezultati_edited  
#prozivnik
#edit tablice profesora
#izbornik za željenu operaciju (unos podataka, izrada prizivnika i sl) 
#popis studenata da se automatizira prisutnost 
#javna nabava
"""
