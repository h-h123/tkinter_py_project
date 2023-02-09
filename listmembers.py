#import webbrowser
from tkinter import Button, Label,Entry,Tk
import os
import datetime
#import shutil
from tkinter import messagebox as msg
from tkinter import simpledialog as sd

import sqlite3
 
sqliteconnection = sqlite3.connect('main_database.db')
cursor = sqliteconnection.cursor()

def listMembers():
    gtk5=Tk()
    cursor.execute("SELECT * FROM User limit 0,10")
    i=0
    for st in cursor:
        for j in range(len(st)):
            e = Label(gtk5,width=10,text=st[j])
            e.grid(row=i,column=j)
            
        i+=1
    gtk5.mainloop()
