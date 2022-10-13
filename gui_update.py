# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 15:27:33 2022

@author: Doria
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


def unos_rezultata_ispit():

        """
        #Dio koda koji dobiva podatke za ispit
        """
        headings_data_ispit = pd.read_csv('grade1.csv', dtype={'JMBAG': str})
        headings_data_list_old_ispit = list(headings_data_ispit)
    
        #debugging
        print("redova:", len(headings_data_ispit))
        print("stupaca:",  len(headings_data_ispit.columns))
    
        test=0
    
        x=495+730
        y1=len(headings_data_ispit)*22+30
        y=y1
        scrl = False
        if y1 >= 700:
            y1 = 700
            scrl = True
            
    
        headings_data_old_ispit = headings_data_ispit
    
        headings_data_ispit = headings_data_ispit.drop(headings_data_ispit.index[range(len(headings_data_ispit))], axis=0)
        headings_data_ispit = headings_data_ispit.drop(headings_data_ispit.columns[range(0,4)], axis=1)
        headings_list_ispit = list(headings_data_ispit)
    
        first_four_columns_ispit = headings_data_old_ispit.drop(headings_data_old_ispit.columns[range(4,9)], axis=1)
    
        first_four_columns_ispit.to_csv('first_four_columns_ispit.csv', sep=',', index=False)
    
        with open('first_four_columns_ispit.csv', newline='', encoding = 'UTF-8') as file:
            reader = csv.reader(file, delimiter = ',')
            headings2_ispit = next(reader)
            first_four_columns_ispit = []
            for row in reader:
                first_four_columns_ispit.append(row[:])
    
    
        #debugging
        print("\nheadings_data_old_ispit:", headings_data_old_ispit, sep='\n')
        print("\nheadings_data_ispit:", headings_data_ispit, sep='\n')
        print("\nheadings_ispit:", headings_list_ispit, sep='\n')
        print("\nfirst_four_columns_ispit:", first_four_columns_ispit, sep='\n')
    
    
        """
        #Dio koda koji obavlja gui
        """
        headings_ispit = headings_list_ispit
        header_list_ispit = headings2_ispit
    
    
        layout_left = [	
            [sg.Table(values=first_four_columns_ispit, headings=header_list_ispit, auto_size_columns=False, col_widths=[4,11,15,15], row_height=22, display_row_numbers=False, justification='center', hide_vertical_scroll=True, num_rows=min(len(first_four_columns_ispit)+test, len(first_four_columns_ispit)+test))]
        	]
    
        naslov=[[sg.Text(h, size=(15,0), justification='center', pad=(0,0)) for h in headings_ispit]]
    
        layout_right = naslov + [
            [sg.Input(size=(15,0), pad=(0,0)) for col in range(len(headings_data_ispit.columns))] for row in range(len(headings_data_old_ispit)+test)
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
#-------------------------------------------------------------------------------------------------------

def unos_rezultata_kolokvij(path):
    """
    #Dio koda koji dobiva podatke za kolokvij
    """
    headings_data_kolokvij = pd.read_csv(path, dtype={'ID broj': str})
    kolokvij = pd.DataFrame()
    
    kolokvij[['Ime', 'Prezime']] = headings_data_kolokvij['Puno ime'].str.split(' ', 1, expand=True)
    kolokvij['JMBAG'] = headings_data_kolokvij['ID broj']
    kolokvij.insert(loc=0, column='RB', value=np.arange(start=1, stop=len(kolokvij)+1, step=1))
    headings_kolokvij = list(kolokvij)
    headings_kolokvij_desno = ['Z1','Z2']
    kolokvij_list = kolokvij.values.tolist()
    
    
    #debugging
    print("redova:", len(headings_data_kolokvij))
    print("stupaca:",  len(headings_data_kolokvij.columns))
    print(kolokvij)
    
    test=0
    
    x1 = 225
    x=495+x1
    y1=len(kolokvij)*22+30
    y=y1
    scrl = False
    if y1 >= 700:
        y1 = 700
        scrl = True
        
    """
    #Dio koda koji obavlja gui
    """ 
     
    layout_left = [	
        [sg.Table(values=kolokvij_list, headings=headings_kolokvij, auto_size_columns=False, col_widths=[4,11,15,15], row_height=22, display_row_numbers=False, justification='center', hide_vertical_scroll=True, num_rows=min(len(kolokvij)+test, len(kolokvij)+test))]
    	]
    
    naslov=[[sg.Text(h, size=(10,0), justification='center', pad=(0,0)) for h in headings_kolokvij_desno]]
    
    layout_right = naslov + [
        [sg.Input(size=(10,0), pad=(0,0)) for col in range(2)] for row in range(len(kolokvij)+test)
                    ] 
    
    layout1 = [
        [sg.Col(layout_left, size=(498,y), scrollable=False), sg.Col(layout_right, size=(x1,y), scrollable=False)],
        ]
    
    layout = [
        [sg.Text('Datum uvida u kolokvij:'), sg.InputText(size=(11,0))],
        [sg.Col(layout1, scrollable=scrl, vertical_scroll_only=True, size=(x,y1))],
        [sg.Submit(), sg.Cancel()]
        ]
    window = sg.Window('Unos podataka s kolokvija', layout, font=("Helvetica", 12), resizable=False)
    button, values = window.Read()
    window.close()
    
#def isvu_download():
    
def kolokvij_odabir():
    layout = [
        [sg.Radio('Kolokvij 1', "RADIO1", 0, key="-IN1-")],
        [sg.Radio('Kolokvij 2', "RADIO1", 0, key="-IN2-")],
        [sg.Radio('Kolokvij 3', "RADIO1", 0, key="-IN3-")],
        [sg.Radio('Kolokvij 4', "RADIO1", 0, key="-IN4-")],
        [sg.Text()],
        [sg.Button("Ok"), sg.Button("Odustani")]
        ]
    window = sg.Window("Odabir kolokvija", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Ok" and values["-IN1-"] == True:
            unos_rezultata_kolokvij('mehanika2/Prijava za prvi kolokvij.csv')
        elif event == "Ok" and values["-IN2-"] == True:
            unos_rezultata_kolokvij('mehanika2/Prijava za drugi kolokvij.csv')
        elif event == "Ok" and values["-IN3-"] == True:
            unos_rezultata_kolokvij('mehanika2/Prijava za treći kolokvij.csv')
        elif event == "Ok" and values["-IN4-"] == True:
            unos_rezultata_kolokvij('mehanika2/Prijava za četvrti kolokvij.csv')
        elif event == "Odustani":
            window.close()
        
    window.close()

def open_window2():
    layout = [[sg.Text("New Window", key="new")]]
    window = sg.Window("Second Window", layout, modal=True)
    choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        
    window.close()    

def main():
    layout = [
        [sg.Radio('Mehanika I', "RADIO1", 0, key="-IN1-"), sg.Radio('Mehanika II', "RADIO1", 0, key="-IN2-"), sg.Radio('Čvrstoća', "RADIO1", 0, key="-IN3-"), sg.Radio('Čvrstoća II', "RADIO1", 0, key="-IN4-"), sg.Radio('Eksperimentalna mehanika', "RADIO1", 0, key="-IN5-"), sg.Radio('Teorija elastičnosti', "RADIO1", 0, key="-IN6-")],
        [sg.Radio('Ispit', "RADIO2", 0, key="-IN11-"), sg.Radio('Kolokvij', "RADIO2", 0, key="-IN12-")],
        [sg.Text()],
        [sg.Text()],
        [sg.Button("Preuzimanje prijavljenih studenata s ISVU Nastavničkog portala")],
        [sg.Button("Preuzimanje prijavljenih studenata s Merlina")],
        [sg.Button("Izrada prozivnika")],
        [sg.Button("Unos rezultata")],
        [sg.Button("Prisutnost")],
        [sg.Text()],
        [sg.Text()],
        [sg.Button("Zatvori"), sg.Push(), sg.Text('Created by: Dorian Turk')]
        ]
    window = sg.Window("Asistent SFSB", layout)
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif values["-IN1-"] == True and event == "Preuzimanje prijavljenih studenata s ISVU Nastavničkog portala":
            print("odabran kolegij je Mehanika I")
            exec(open("web_M1.py").read())
            print("popis studenata je preuzet")
            exec(open("grade1.py").read())
            print("dobiven je dokument grade1.csv")
            
        elif values["-IN2-"] == True and event == "Preuzimanje prijavljenih studenata s ISVU Nastavničkog portala":
            print("odabran kolegij je Mehanika II")
            exec(open("web_M2.py").read())
            print("popis studenata je preuzet")
            exec(open("grade1.py").read())
            print("dobiven je dokument grade1.csv")
        
        elif event == "Unos rezultata" and values["-IN12-"] == True:
            kolokvij_odabir()
            
        elif event == "Preuzimanje prijavljenih studenata s Merlina" and values["-IN12-"] == True:
            kolokvij_odabir()
         
        elif event == "Unos rezultata" and values["-IN11-"] == True:
            unos_rezultata_ispit()
            
        elif event == "open2":
            open_window2()
        
        elif event == "Zatvori":
            window.close()
        

if __name__ == "__main__":
    main()