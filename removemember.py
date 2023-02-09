#import webbrowser
#from tkinter import Button, Label,Entry,Tk
import os
import datetime
import shutil
from tkinter import messagebox as msg
from tkinter import simpledialog as sd
import sqlite3
 
sqliteconnection = sqlite3.connect('main_database.db')
cursor = sqliteconnection.cursor()

def rndm():
	return str(datetime.datetime.now()).replace(" ","").replace("-","").replace(".","").replace(":","")



def removeMember():
	w=sd.askstring("Remove member","Enter member id")
	w = str(w)
	print(type(w))
	if w>'0':
		cursor.execute('delete from User where user_id=?',(w,))
		sqliteconnection.commit()
		msg.showinfo("Remove member","Member removed successfully")
	else:
		msg.showerror("Remove member","Member not found")