
# Written by Nicholas Johansan
# made to try sqlite3 and tkinter
# just a simple login/register system

from tkinter import *
from tkinter import messagebox
import sqlite3

login = Tk()
login.title("")
login.geometry("225x145+25+80")

#create or connect database
conn = sqlite3.connect('login.db')

#create cursor
c = conn.cursor()

#create table
'''
c.execute("""CREATE TABLE credentials (
		user_name text,
		password text
		)""")
'''

def logout_func():
	
	main.destroy()

	global login
	login = Tk()
	login.title("")
	login.geometry("225x145+25+80")

	# Labels constructions
	title_lbl_login = Label(login, text="Log In / Sign Up", font=("Helvetica", 12))
	title_lbl_login.grid(row=0, column=0, columnspan=2, pady=(10, 0))

	username_lbl_login = Label(login, text="Username:", font=("Helvetica", 10))
	username_lbl_login.grid(row=1, column=0, padx=(10, 0))

	password_lbl_login = Label(login, text="Password: ", font=("Helvetica", 10))
	password_lbl_login.grid(row=2, column=0, padx=(10, 0))
	#show="*"
	#Entry Boxes
	global username_entry_login
	username_entry_login = Entry(login)
	username_entry_login.grid(row=1, column=1)

	global password_entry_login
	password_entry_login = Entry(login, show="*")
	password_entry_login.grid(row=2, column=1)

	#Buttons
	login_btn_login = Button(login, text="Log In", font=("Helvetica", 10), command=login_func, padx=65)
	login_btn_login.grid(row=3, columnspan=2)

	signup_btn_login = Button(login, text="Sign Up", font=("Helvetica", 10), command=signup_func, padx=60)
	signup_btn_login.grid(row=4, columnspan=2)

#Functions
def login_func():

	if username_entry_login.get() == "":
		messagebox.showinfo("Info", "You have not entered your username.")
		return
	elif password_entry_login.get() == "":
		messagebox.showinfo("Info", "You have not entered your password.")
		return
	else:
		pass

	#create or connect database
	conn = sqlite3.connect('login.db')
	#create cursor
	c = conn.cursor()

	c.execute(f"SELECT * FROM credentials WHERE user_name = '{username_entry_login.get()}' AND password = '{password_entry_login.get()}'")
	results = c.fetchall()

	if len(results) == 0:
		username_entry_login.delete(0, END)
		password_entry_login.delete(0, END)
		messagebox.showinfo("Info", "You have not signed up before, please sign up first.")
		return
	else:
		name = username_entry_login.get()
		messagebox.showinfo("Info", "Successfully logged in.")
		login.destroy()
		global main
		main = Tk()
		main.title("")
		main.geometry("200x100+25+80")
		welcome_lbl_main = Label(main, text=f"Welcome back, {name}!", font=("Helvetica", 10))
		welcome_lbl_main.grid(row=0, column=0, padx=(10, 0), pady=(10, 0))
		logout_btn_main = Button(main, text="Log Out", font=("Helvetica", 10), command=logout_func, padx=60)
		logout_btn_main.grid(row=1, column=0, padx=(10, 0))


	#commit changes
	conn.commit()

	#close connection
	conn.close()

def signup_func():

	if username_entry_login.get() == "":
		messagebox.showinfo("Info", "You have not entered your username.")
		return
	elif password_entry_login.get() == "":
		messagebox.showinfo("Info", "You have not entered your password.")
		return
	else:
		pass

	#create or connect database
	conn = sqlite3.connect('login.db')
	#create cursor
	c = conn.cursor()

	c.execute(f"SELECT * FROM credentials WHERE user_name = '{username_entry_login.get()}' AND password = '{password_entry_login.get()}'")
	results = c.fetchall()

	if len(results) == 0:
		c.execute(f"INSERT INTO credentials VALUES ('{username_entry_login.get()}', '{password_entry_login.get()}')")
		username_entry_login.delete(0, END)
		password_entry_login.delete(0, END)
		messagebox.showinfo("Info", "Signed up successfully.")
	else:
		username_entry_login.delete(0, END)
		password_entry_login.delete(0, END)
		messagebox.showinfo("Info", "You have already signed up, please log in.")
		return


	#commit changes
	conn.commit()

	#close connection
	conn.close()

# Labels constructions
title_lbl_login = Label(login, text="Log In / Sign Up", font=("Helvetica", 12))
title_lbl_login.grid(row=0, column=0, columnspan=2, pady=(10, 0))

username_lbl_login = Label(login, text="Username:", font=("Helvetica", 10))
username_lbl_login.grid(row=1, column=0, padx=(10, 0))

password_lbl_login = Label(login, text="Password: ", font=("Helvetica", 10))
password_lbl_login.grid(row=2, column=0, padx=(10, 0))
#show="*"
#Entry Boxes
username_entry_login = Entry(login)
username_entry_login.grid(row=1, column=1)

password_entry_login = Entry(login, show="*")
password_entry_login.grid(row=2, column=1)

#Buttons
login_btn_login = Button(login, text="Log In", font=("Helvetica", 10), command=login_func, padx=65)
login_btn_login.grid(row=3, columnspan=2)

signup_btn_login = Button(login, text="Sign Up", font=("Helvetica", 10), command=signup_func, padx=60)
signup_btn_login.grid(row=4, columnspan=2)

#commit changes
conn.commit()

#close connection
conn.close()

login.mainloop()
