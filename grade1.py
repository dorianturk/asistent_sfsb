# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 14:49:31 2022

@author: zsk
"""
import pandas as pd
import numpy as np
import glob
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