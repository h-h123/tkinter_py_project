#import webbrowser
from tkinter import Button, Label,Entry,Tk
import os
import datetime
#import shutil
from tkinter import messagebox as msg
from tkinter import simpledialog as sd

def rndm():
	return str(datetime.datetime.now()).replace(" ","").replace("-","").replace(".","").replace(":","")

import sqlite3
 
sqliteconnection = sqlite3.connect('main_database.db')
cursor = sqliteconnection.cursor()


def assignBook():
	gtk3=Tk()
	gtk3.title("Assign book")
	gtk3.geometry("600x200")
	Label(gtk3, height="200", width="2000", background="green").place(x=0,y=0)
	#Label(gtk3, text="Enter member name", font=("Bahnschrift","15"), background="green").place(x=20,y=20)
	Label(gtk3, text="Enter member id", font=("Bahnschrift","15"), background="green").place(x=20,y=20)
	Label(gtk3, text="Enter book id", font=("Bahnschrift","15"), background="green").place(x=20,y=70)
	def assignBookFunc():

		# user_id = w[0].get()
		# book_id= w[1].get()
		# sqlform = """insert into User(user_id,book_id) values (?,?);"""
		# data = (user_id,book_id)
		# cursor.execute(sqlform,data)
		# sqliteconnection.commit()
		# sqliteconnection.close()
		mmid = w[0].get()
		bkid = w[1].get()
		cursor.execute('select book_allocated from User where user_id=?',(mmid,))
		myresult = cursor.fetchone()[0]

		cursor.execute('select user_id from Book where book_id=?',(bkid,))
		myresult2 = cursor.fetchone()[0]
		# if myresult[3] == 0:
		#     print('here all set')
		if myresult == 0:
			if myresult2 == 0:
				cursor.execute('update User set book_allocated=? where user_id=?',(1,mmid,))
				cursor.execute('update Book set user_id=? where book_id=?',(mmid,bkid,))
			
			else:
				msg.showerror("Error","book not available")
		
		else:
			msg.showerror("Error","book already assigned")

			
		sqliteconnection.commit()
		#sqliteconnection.close()  



		# e=[w[0].get(), w[1].get()]
		# bln =[((w[0].get() in os.listdir("members")) , (w[1].get() in os.listdir("books")) , (open("books/"+e[1]+"/available","r").read() == "0") , (open("members/"+e[0]+"/book","r").read() == "0"))]
		# if False not in bln:
		# 	book_name=open("books/"+e[1]+"/name","r").read()
		# 	open("members/"+e[0]+"/book","w").write(f"{book_name}\n{e[1]}")
		# 	open("books/"+e[1]+"/available","w").write(e[0])
		# 	msg.showinfo("Assign book","Book assigned successfully.")
		# 	gtk3.destroy()
		# else:
		# 	msg.showerror("Error","Cannot assign book")
	w = [Entry(gtk3, bd=3, font=("Bahnschrift","15")),Entry(gtk3, bd=3, font=("Bahnschrift","15"))]
	Button(gtk3, text="Assign book", font=("Bahnschrift","15"), command=assignBookFunc).place(x=20,y=130)
	w[0].place(x=230, y=20)
	#w[1].place(x=230, y=40)
	w[1].place(x=230, y=70)
	gtk3.mainloop()