import webbrowser
from tkinter import Button, Label,Entry,Tk
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



# def removeMember():
	
# 	w=sd.askstring("Remove member","Enter member id")
# 	w = str(w)
# 	#print(type(w))
# 	if w>'0':
# 		cursor.execute('delete from User where user_id=?',(w,))
# 		sqliteconnection.commit()
# 		msg.showinfo("Remove member","Member removed successfully")
# 	else:
# 		msg.showerror("Remove member","Member not found")
	
############################################################################

def removeMember():
	gtk2=Tk()
	gtk2.title("Remove Member")
	gtk2.geometry("600x200")
	Label(gtk2, height="200", width="2000", background="green").place(x=0,y=0)
	Label(gtk2, text="Enter User_id", font=("Bahnschrift","15"), background="green").place(x=20,y=20)
	Label(gtk2, text="Enter User_name", font=("Bahnschrift","15"), background="green").place(x=20,y=70)
	
	def removememberFunc():
		user_id = w[0].get()
		user_name = w[1].get()
		try:
			cursor.execute('DELETE FROM User WHERE user_id=? AND user_name=?', (user_id, user_name))
			sqliteconnection.commit()
			msg.showinfo("Remove member", "Member removed successfully")
		except sqlite3.Error as error:
			msg.showerror("Remove member", "Error removing member: " + str(error))
		gtk2.destroy()

	w = [Entry(gtk2, bd=3, font=("Bahnschrift","15")),Entry(gtk2, bd=3, font=("Bahnschrift","15"))]
	Button(gtk2, text="Remove Member", font=("Bahnschrift","15"), command=removememberFunc).place(x=20,y=130)
	w[0].place(x=230, y=20)
	w[1].place(x=230, y=70)
	gtk2.mainloop()
