from tkinter import *
from tkinter import messagebox
import math
from password_gen import generate_password
import pyperclip
#importing jason module
import json



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    password=generate_password()
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_entries():

    website=website_entry.get()
    passwd=password_entry.get()
    usremail=email_entry.get()
    #setting the data as dictionary
    new_entry={
        website:{
            "password":passwd,
            "email":usremail
            
        }
    }

    if len(website)== 0 or len(passwd)== 0:
        messagebox.showinfo(title="Ooops",message="Do not leave and fields blank")
    else:
        proceed=messagebox.askokcancel(title="Final check",message=f"details entered:\nWebsite:{website}\nEmail:{usremail}\nPassword:{passwd}|\nConfirm to proced to save")
        if proceed ==True:
            #first lets try to read if a file exits 
            try:
                with open("data.json","r") as datafile:
                    #load the current data
                    current_data=json.load(datafile)
            except FileNotFoundError:
                #if no json file command to creat one
                with open("data.json","w") as datafile:
                    json.dump(new_entry,datafile,indent=4)
            else:
                #if file exist we will update the data 
                current_data.update(new_entry)
                #now lets update the files 
                with open("data.json","w") as datafile:
                    json.dump(current_data,datafile,indent=4)
            finally:
                website_entry.delete(0,END)
                password_entry.delete(0,END)
#-----------------------------SEARCH ----------------------------------#
def find_password():
    web=website_entry.get()
    try:
        with open("data.json","r") as datafile:
            data_file=json.load(datafile)
    except FileNotFoundError:
        messagebox.showinfo (title="error",message=f"No data file found")
    else:
        if web in data_file:
            email=data_file[web]["email"]
            passwd=data_file[web]["password"]
            messagebox.showinfo (title="info",message=f"email:{email}\npassword:{passwd}")
        else:
            messagebox.showinfo (title="error",message=f"No record for {web}")
        






# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password safe")
window.config(padx=50,pady=50)

canvas=Canvas(width=220, height=220,bg="white",highlightthickness=0)
# need to create a image variable . Only this kind of variable can be incented to canvas class as an image
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1,row=0)

# --------------------------SETTING UP LABALS

#setting the website labal
website_lb=Label(text="Website:")
website_lb.grid(row=1,column=0)

#setting the Email labal
email_lb=Label(text="Email/Username")
email_lb.grid(row=2,column=0)

#setting the Password labal
Password_lb=Label(text="Password")
Password_lb.grid(row=3,column=0)

# ------------------------SETTING UP ENTRIES
# website entry
website_entry=Entry(width=21)
website_entry.grid(row=1,column=1)
website_entry.focus()

#email entry
email_entry=Entry(width=37)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"shashika.rathnasinghe@gmail.com")

#email entry
password_entry=Entry(width=21)
password_entry.grid(row=3,column=1)

#------------------------ SETTING UP BUTTONS
# generate passwords button
gen_pw=Button(text="Generate Passwords",highlightthickness=-0,width=12,command=gen_password)
gen_pw.grid(row=3,column=2)

# add button
add_b=Button(text="ADD",highlightthickness=-0,width=36,command=save_entries)
add_b.grid(row=4,column=1,columnspan=2)

search_but=Button(text="Search",highlightthickness=-0,width=8,command=find_password)
search_but.grid(row=1,column=2)









window.mainloop()

