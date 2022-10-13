# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 14:50:12 2022

@author: zsk
"""
import PySimpleGUI as sg
import pandas as pd
import csv
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
if y1 >= 700:
    y1 = 700
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