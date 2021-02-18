import random
from tkinter import*

window=Tk()
window.geometry("750x500")
window.title("Dice Roller")
l1=Label(window,text="",font=("times new roman",350))
l1.place(x=200,y=0)

def roll_fun():
    number=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    l1.config(text=f'{random.choice(number)}')
    l1.pack()

b1=Button(window,text="Lets Roll",command=roll_fun)
b1.place(x=330,y=0)

window.mainloop()