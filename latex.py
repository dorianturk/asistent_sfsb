# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 14:52:51 2022

@author: zsk
"""
import pandas as pd
import os
import datetime
import calendar
from googletrans import Translator
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