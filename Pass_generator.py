import random
import string
from tkinter import *

import pyperclip


def generator():
    small_alphabets=string.ascii_lowercase
    capital_alphabets=string.ascii_uppercase
    numbers=string.digits
    special_charecters=string.punctuation

    all=small_alphabets+capital_alphabets+numbers+special_charecters
    password_length=int(length_Box.get())

    if choice.get()==1:
        passwordField.insert(0,random.sample(small_alphabets,password_length))

    if choice.get()==2:
        passwordField.insert(0,random.sample(small_alphabets+capital_alphabets,password_length))

    if choice.get()==3:
        passwordField.insert(0,random.sample(all,password_length))


def copy():
    random_password=passwordField.get()
    pyperclip.copy(random_password)

root=Tk()
root.title("Random Password Generator")

root.geometry("400x300")
choice=IntVar()
Font=('arial',13,'bold')
frame=LabelFrame(root,text='Password Strenght',font=('times new roman',20,'bold'))
frame.pack()
weakradioButton=Radiobutton(frame,text='Weak',value=1,variable=choice,font=Font)
weakradioButton.pack(anchor=W)

mediumradioButton=Radiobutton(frame,text='Medium',value=2,variable=choice,font=Font)
mediumradioButton.pack(anchor=W)

strongradioButton=Radiobutton(frame,text='Strong',value=3,variable=choice,font=Font)
strongradioButton.pack(anchor=W)

lengthLabel=Label(root,text='Password Length:',font=Font)
lengthLabel.pack()

length_Box=Spinbox(root,from_=8,to_=24,width=5,font=Font)
length_Box.pack()

generateButton=Button(root,text='Generate',font=Font,command=generator)
generateButton.place_configure(x=153, y=180)

passwordField=Entry(root,width=25,bd=2,font=Font)
passwordField.place_configure(x=80, y=220)

copyButton=Button(root,text='Copy',font=Font,command=copy)
copyButton.place_configure(x=170, y=250)

root.mainloop()