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



def rndm():
	return str(datetime.datetime.now()).replace(" ","").replace("-","").replace(".","").replace(":","")


def addBook():
	gtk2=Tk()
	gtk2.title("Add book")
	gtk2.geometry("600x200")
	Label(gtk2, height="200", width="2000", background="green").place(x=0,y=0)
	Label(gtk2, text="Enter name", font=("Bahnschrift","15"), background="green").place(x=20,y=20)
	Label(gtk2, text="Enter author", font=("Bahnschrift","15"), background="green").place(x=20,y=70)
	def addBookFunc():
		e = rndm()
		# os.mkdir("books/"+e)
		# open("books/"+e+"/name","a").write(w[0].get())
		# open("books/"+e+"/author","a").write(w[1].get())
		# open("books/"+e+"/available","a").write("0")
		book_name = w[0].get()
		author_name = w[1].get()
		sqlform = """insert into Book(book_name,author_name) values (?,?);"""
		data = (book_name,author_name)
		cursor.execute(sqlform,data)
		sqliteconnection.commit()
		#sqliteconnection.close()

		msg.showinfo("Add book",f"Book added successfully.")
		gtk2.destroy()
	w = [Entry(gtk2, bd=3, font=("Bahnschrift","15")),Entry(gtk2, bd=3, font=("Bahnschrift","15"))]
	Button(gtk2, text="Add book", font=("Bahnschrift","15"), command=addBookFunc).place(x=20,y=130)
	w[0].place(x=230, y=20)
	w[1].place(x=230, y=70)
	gtk2.mainloop()