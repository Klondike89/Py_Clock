from tkinter import *
import time


window = Tk()

def get_time():
    display_time= time.strftime("%A %Y-%m-%d  %I:%M:%S %p")
    clock.config(text=display_time)
    clock.after(20, get_time)
    
C = Canvas(window, bg="blue",height="880",width="1700")
C.pack(fill = "both", expand = True)
filename = PhotoImage(file = r"C:\Users\brian\Desktop\PYTHON\Py_Clock\US-Time-Zone-Map.png")
C.create_image(0, 0, image = filename, anchor = "nw")

clock = Label(window, fg="white", bg="black", font = "Hurmit_NF 50", width=30, height=2)
clock.place(x=100,y=500)

get_time()

window.mainloop()
