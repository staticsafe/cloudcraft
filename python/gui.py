from tkinter import *
from tkinter.ttk import *

root = Tk()
    
startbutton = Button()
stopbutton = Button()
webstartbutton = Button()
serverstatus = Label()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)

root.config(menu=menubar)
startbutton.config(text='Start Server')
stopbutton.config(text='Stop Server')
webstartbutton.config(text='Start WebServer')

filemenu.add_command(label='Quit')
menubar.add_cascade(label='File', menu=filemenu)

serverstatus.pack()
startbutton.pack(side='right')
stopbutton.pack(side='right')
webstartbutton.pack(side='right')

root.mainloop()
