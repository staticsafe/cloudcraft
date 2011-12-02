from tkinter import *
from tkinter.ttk import *
import subprocess

class Application(Frame):
    def start_server(self):
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = subprocess.SW_HIDE
        server = ('python main.py')
        try:
            process = subprocess.Popen(server, startupinfo=startupinfo)
        except:
            return 'already running'
        
    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "Quit"
        self.QUIT["command"] = self.quit

        self.QUIT.pack({"side": "left"})

        self.start = Button(self)
        self.start["text"] = "Start",
        self.start["command"] = self.start_server

        self.start.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
