#coding=UTF-8
from select import select
import tkinter as tk 
import os
from tkinter import Button, filedialog as fd
from tkinter import messagebox
from tkinter import ttk
from turtle import title


window=tk.Tk()
window.title("Picpick")
window.geometry('800x600')
window.configure(background='gray')


def select_file():
    filetypes=(
        ('folder')
    )

    filename=fd.askopenfilename(
        title="open file",
        initialdir="/",
        filetypes=filetypes
    )

    messagebox.showinfo(
        title='selected file',
        message=filename
    )

#open 
open_button= ttk.Button(
    window,
    text="開啟資料夾",
    command=select_file    
)

open_button.pack(expand=True)

#run the app
window.mainloop()