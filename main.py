# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 14:48:32 2022

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



exec(open("web.py").read())
exec(open("grade1.py").read())
exec(open("gui.py").read())
exec(open("grade.py").read())
exec(open("latex.py").read())
exec(open("latex.py").read())
exec(open("move_data.py").read())


"""
#Ideje:
#edit samo file rezultati_edited  
#prozivnik
#edit tablice profesora
#izbornik za željenu operaciju (unos podataka, izrada prizivnika i sl) 
#popis studenata da se automatizira prisutnost 
#javna nabava
"""
