# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 14:51:57 2022

@author: zsk
"""

import pandas as pd
import numpy as np

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