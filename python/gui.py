from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('Server Manager')
root.resizable(width=FALSE,height=FALSE)

def start_server():
    pass
def stop_server():
    pass


frame = Frame()
startbutton = Button(frame)
stopbutton = Button(frame)
webstartbutton = Button(frame)
webstopbutton = Button(frame)
mcstartbutton = Button(frame)
mcstopbutton = Button(frame)
serverstatus = Label(frame)
webserverstatus = Label(frame)
mcserverstatus = Label(frame)
seperator = Label(frame)
seperator2 = Label(frame)
seperator3 = Label(frame)
seperator4 = Label(frame)
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
optionsmenu = Menu(menubar, tearoff=0)

root.config(menu=menubar)
serverstatus.config(text='Main Server', font=('segoe ui',12))
webserverstatus.config(text='Web Server', font=('segoe ui',12))
mcserverstatus.config(text='Minecraft Server', font=('segoe ui',12))
startbutton.config(text='Start')
stopbutton.config(text='Stop')
webstartbutton.config(text='Start')
webstopbutton.config(text='Stop')
mcstartbutton.config(text='Start')
mcstopbutton.config(text='Stop')

menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Quit', command=root.destroy)
menubar.add_cascade(label='Options', menu=optionsmenu)
menubar.add_command(label="Help")


frame.pack()
seperator4.grid(column=0, row=0)
serverstatus.grid(column=0,row=1,rowspan=2)
webserverstatus.grid(column=0,row=4,rowspan=2)
mcserverstatus.grid(column=0,row=7, rowspan=2, padx=15)
startbutton.grid(column=2,row=1)
stopbutton.grid(column=2,row=2)
seperator.grid(column=2,row=3, padx=55, pady=5)
webstartbutton.grid(column=2,row=4)
webstopbutton.grid(column=2,row=5)
seperator2.grid(column=2,row=6, padx=55, pady=5)
mcstartbutton.grid(column=2,row=7)
mcstopbutton.grid(column=2,row=8)
seperator3.grid(column=2,row=9, padx=55, pady=0)


root.mainloop()
