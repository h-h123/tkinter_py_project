from tkinter import Button, Label, Entry, Tk
import os
import datetime
# import shutil
from tkinter import messagebox as msg
from tkinter import simpledialog as sd

import sqlite3

sqliteconnection = sqlite3.connect('main_database.db')
cursor = sqliteconnection.cursor()


def SearchBook():
	gtk2=Tk()
	gtk2.title("Search book")
	gtk2.geometry("600x200")
	Label(gtk2, height="200", width="2000", background="green").place(x=0,y=0)
	Label(gtk2, text="Enter book name", font=("Bahnschrift","15"), background="green").place(x=20,y=20)
	Label(gtk2, text="Enter author name", font=("Bahnschrift","15"), background="green").place(x=20,y=70)
	def addBookFunc():
		book_name = w[0].get()
		author_name = w[1].get()
		cursor.execute('select user_id from Book where book_name=? and author_name=?',(book_name,author_name,))
		myresult2 = cursor.fetchone()[0]
		sqliteconnection.commit()

		if myresult2==0:
			msg.showinfo("Search book",f"Book is Available.")
		else:
			msg.showinfo("Search book",f"Book is not Available.")

		#sqliteconnection.close()
		gtk2.destroy()
	w = [Entry(gtk2, bd=3, font=("Bahnschrift","15")),Entry(gtk2, bd=3, font=("Bahnschrift","15"))]
	Button(gtk2, text="Search book", font=("Bahnschrift","15"), command=addBookFunc).place(x=20,y=130)
	w[0].place(x=230, y=20)
	w[1].place(x=230, y=70)
	gtk2.mainloop()