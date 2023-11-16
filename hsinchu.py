import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from tkinter import *
import tkinter as tk
from tkinter import scrolledtext

def north_button_check():
    select('北區')

def east_button_check():
    select('東區')

def Xiangshan_button_check():
    select('香山區')

def select(area):
    df = pd.read_csv("df/hsinchu.csv",encoding='utf-8')
    rows = df['行政區'] == area
    colums = ('名稱' ,'網址' ,'電話' ,'地址')
    result = df.loc[rows,colums]

    new_windows = tk.Toplevel(windows)
    out_text = scrolledtext.ScrolledText(new_windows, width=120, height=30, wrap=tk.WORD)
    out_text.insert(tk.END, result)
    out_text.pack()

windows = Tk()
windows.title('hsinchu')
windows.geometry('500x500')
windows.resizable(width=False,height=False)
north_button = Button(text="北區",font=("Arial", 14, "bold"),command=north_button_check)
east_button = Button(text='東區',font=("Arial", 14, "bold"),command=east_button_check)
Xiangshan_button = Button(text="香山區",font=("Arial", 14, "bold"),command=Xiangshan_button_check)
north_button.pack()
east_button.pack()
Xiangshan_button.pack()
windows.mainloop()