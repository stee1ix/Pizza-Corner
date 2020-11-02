from tkinter import *
from PIL import ImageTk,Image
import os
import sys 


root = Tk()
root.title("Pizza Corner!")
root.geometry("800x540+200+50")
root.resizable(False,False)
root.iconbitmap('images/pizza.ico')

myImg=ImageTk.PhotoImage(Image.open("images/PIZZA.png"))
my_label =Label(root,image=myImg)
my_label.pack(pady=10,padx=10)

frame=LabelFrame(root,text='Pizza Corner!',font='Lora',padx=180,pady=50,bd=4)
frame.pack()

def connectOrder():
	os.system('python main/main.py')

Order_Pizza=Button(frame,font=("Lora",10),relief=GROOVE, text='  Welcome to Pizza-Corner  ',height=3,width=20,bd=4,bg='#7ea04d',activebackground='#7ea04d',command=connectOrder)

myLabel1=Label(frame,text="  ")
myLabel2=Label(frame,text="  ")

Order_Pizza.grid(row=0, column=0)
myLabel1.grid(row=0,column=1)


root.mainloop()
