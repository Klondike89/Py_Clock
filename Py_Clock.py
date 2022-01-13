from tkinter import *
import time


window = Tk()

def get_time():
    display_time= time.strftime("%A %Y-%m-%d  %I:%M:%S %p")
    clock.config(text=display_time)
    clock.after(20, get_time)
    

clock = Label(window, fg="white", bg="black", font = "Hurmit_NF 50", width=30, height=5)
clock.pack()

get_time()

window.mainloop()
