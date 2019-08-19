import pandas as pd
import re
import numpy as np
import csv
from pandas import ExcelWriter
from pandas import ExcelFile
from openpyxl import load_workbook

import easygui
import sys
from easygui import *
#easygui.egdemo()
#print(easygui.fileopenbox())
file_loc = easygui.fileopenbox() 
df = pd.read_csv(file_loc)
#print(df)
msg = " Please select the required fields "
title = " Excel column trimmer"
choices = df
while 1:
    choice = []
    choice = multchoicebox(msg,title,choices)
    if choice is None:
        sys.exit(0)
    #msgbox("you chose: {}".format(choice), "Survey result")
    else:
        
        print('choices',choice)
        file_save = easygui.filesavebox()
        file_saved = file_save+'.csv'
        print(file_saved)
        pd.read_csv(file_loc,usecols=choice).to_csv(file_saved,index = False)

