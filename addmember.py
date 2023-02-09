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



def addMember():
	gtk1=Tk()
	gtk1.title("Add member")
	gtk1.geometry("600x200")
	Label(gtk1, height="200", width="2000", background="green").place(x=0,y=0)
	Label(gtk1, text="Enter name", font=("Bahnschrift","15"), background="green").place(x=20,y=20)
	Label(gtk1, text="Enter phone number", font=("Bahnschrift","15"), background="green").place(x=20,y=70)
	def addMemberFunc():
		username = w[0].get()
		contact = w[1].get()
		sqlform = """insert into User(user_name,contact) values (?,?);"""
		data = (username,contact)
		cursor.execute(sqlform,data)
		sqliteconnection.commit()
		#sqliteconnection.close()

		msg.showinfo("Add",f"Member added successfully.")
		gtk1.destroy()
	Button(gtk1, text="Create member", font=("Bahnschrift","15"), command=addMemberFunc).place(x=20,y=130)
	w = [Entry(gtk1, bd=3, font=("Bahnschrift","15")),Entry(gtk1, bd=3, font=("Bahnschrift","15"))]
	w[0].place(x=230, y=20)
	w[1].place(x=230, y=70)
	gtk1.mainloop()