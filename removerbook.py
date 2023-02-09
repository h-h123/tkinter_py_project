#import webbrowser
from tkinter import Button, Label,Entry,Tk
import os
import datetime
import shutil
from tkinter import messagebox as msg
from tkinter import simpledialog as sd


import sqlite3
 
sqliteconnection = sqlite3.connect('main_database.db')
cursor = sqliteconnection.cursor()

def removeBook():
	gtk7=Tk()
	gtk7.title("Remove Book")
	gtk7.geometry("800x200")
	Label(gtk7, height="200", width="2000", background="green").place(x=0,y=0)
	Label(gtk7, text="Enter book_id", font=("Bahnschrift","15"), background="green").place(x=20,y=20)
	Label(gtk7, text="Enter book_name", font=("Bahnschrift","15"), background="green").place(x=20,y=70)
	Label(gtk7, text="Enter author_name", font=("Bahnschrift","15"), background="green").place(x=20,y=120)
	
	def removebookFunc():
		book_id = w[0].get()
		book_name = w[1].get()
		author_name = w[2].get()
		try:
			cursor.execute('DELETE FROM Book WHERE book_id=? AND book_name=? AND author_name=?', (book_id, book_name, author_name))
			sqliteconnection.commit()
			msg.showinfo("Remove Book", "Book removed successfully")
		except sqlite3.Error as error:
			msg.showerror("Remove Book", "Error removing book: " + str(error))
		gtk7.destroy()

	w = [Entry(gtk7, bd=3, font=("Bahnschrift","15")),Entry(gtk7, bd=3, font=("Bahnschrift","15")), Entry(gtk7, bd=3, font=("Bahnschrift","15"))]
	Button(gtk7, text="Remove Book", font=("Bahnschrift","15"), command=removebookFunc).place(x=20,y=170)
	w[0].place(x=230, y=20)
	w[1].place(x=230, y=70)
	w[2].place(x=230, y=120)
	gtk7.mainloop()





#################################################################################
# def removeBook():
# 	w=sd.askstring("Remove book","Enter book id")
# 	w = str(w)
# 	print(type(w))
# 	if w>'0':
# 		cursor.execute('delete from Book where book_id=?',(w,))
# 		sqliteconnection.commit()
# 		msg.showinfo("Remove book",f"Book removed successfully")
# 	else:
# 		msg.showerror("Remove book","Book not found")

# ####################################################################
# def removeBook():
# 	gtk7=Tk()
# 	gtk7.title("Remove Book")
# 	gtk7.geometry("600x200")
# 	Label(gtk7, height="200", width="2000", background="green").place(x=0,y=0)
# 	Label(gtk7, text="Enter User_id", font=("Bahnschrift","15"), background="green").place(x=20,y=20)
# 	Label(gtk7, text="Enter User_name", font=("Bahnschrift","15"), background="green").place(x=20,y=70)
	
# 	def removebookFunc():
# 		book_id = w[0].get()
# 		book_name = w[1].get()
# 		try:
# 			cursor.execute('DELETE FROM Book WHERE book_id=? AND book_name=?', (book_id, book_name))
# 			sqliteconnection.commit()
# 			msg.showinfo("Remove Book", "Book removed successfully")
# 		except sqlite3.Error as error:
# 			msg.showerror("Remove Book", "Error removing book: " + str(error))
# 		gtk7.destroy()

# 	w = [Entry(gtk7, bd=3, font=("Bahnschrift","15")),Entry(gtk7, bd=3, font=("Bahnschrift","15"))]
# 	Button(gtk7, text="Remove Book", font=("Bahnschrift","15"), command=removebookFunc).place(x=20,y=130)
# 	w[0].place(x=230, y=20)
# 	w[1].place(x=230, y=70)
# 	gtk7.mainloop()