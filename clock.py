from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("clock")

def time():
    string = strftime('%I:%M:%S %p')
    Label.config(text=string)
    Label.after(1000, time)

Label = Label(root,font=("Algerian", 80), background = "black", foreground = "cyan")
Label.pack(anchor='center')
time()

mainloop()