import webbrowser
from tkinter import Button, Label,Entry,Tk,ttk
import os
import datetime
import shutil
from tkinter import messagebox as msg
from tkinter import simpledialog as sd


import sqlite3
try: 
    sqliteconnection = sqlite3.connect('main_database.db')
    cursor = sqliteconnection.cursor()
    query = 'select sqlite_version();'
    cursor.execute(query)
    result = cursor.fetchall()
    print('SQLite Version is {}'.format(result))
    cursor.close()


except sqlite3.Error as error:
    print(error)

#from tkinter import *
#from PIL import ImageTk, ImageTk

top = Tk()

top.title("Library Management App")
top.geometry("700x400")


Label(top,background="green", foreground="white",font=("Arial","23"), text="Library Management App").place(x=20,y=0)
##################################################################################################################################################

# Import module 
from tkinter import *  
# Adjust size 
#top.geometry("700x700")
  
# Add image file
bg = PhotoImage(file = "bglib.png")
  
# Show image using label
label1 = Label( top, image = bg)
label1.place(x = 0, y = 0)

##################################################################################################################################################
canvas= Canvas(top, width= 1200, height= 40)
#Add a text in Canvas
canvas.create_text(620, 25, text="Library Management System", fill="black", font=('Helvetica 15 bold'))
canvas.pack()


#########################################################################################
import addmember, removerbook, removemember, assignbook, addbook, listmembers, listbooks, removedue,searchbook


Button(top, text="Add member", background="black", foreground="white", font=("Bahnschrift","15"), command=addmember.addMember).place(x=20,y=80)
Button(top, text="Remove member", background="black", foreground="white", font=("Bahnschrift","15"), command=removemember.removeMember).place(x=20,y=160)

Button(top, text="Add book", background="black", foreground="white", font=("Bahnschrift","15"), command=addbook.addBook).place(x=20,y=240)
Button(top, text="Remove book", background="black", foreground="white", font=("Bahnschrift","15"), command=removerbook.removeBook).place(x=20,y=320)

Button(top, text="Assign book", background="black", foreground="white", font=("Bahnschrift","15"), command=assignbook.assignBook).place(x=20,y=400)


Button(top, text="List members", background="black", foreground="white", font=("Bahnschrift","15"),command=listmembers.listMembers).place(x=20,y=480)
Button(top, text="List books", background="black", foreground="white", font=("Bahnschrift","15"),command=listbooks.listBooks).place(x=20,y=560)
Button(top, text="Search books", background="black", foreground="white", font=("Bahnschrift","15"),command=searchbook.SearchBook).place(x=20,y=640)


top.mainloop()

