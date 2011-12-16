from tkinter import *
from tkinter.messagebox import showerror, showwarning
from tkinter.ttk import *
from os import remove, path, name
import psutil
import subprocess
import webbrowser

root = Tk()
root.title('Server Manager')
root.resizable(width=FALSE,height=FALSE)

def web_start():
    if path.isfile('../apache/logs/httpd.pid') == False:
        if os.name == 'nt':
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            try: apachepid = subprocess.Popen('../apache/bin/httpd.exe', startupinfo=startupinfo).pid
            except: showerror('Error', 'Apache could not launch.')
            else: webbrowser.open('http://localhost:8080')
        else: pass
    else: showwarning('Warning', 'Apache is already running.')

def web_stop():
    apache = pid_man('get', 'apache')
    apacheproc = psutil.Process(apache)
    try: apacheproc.terminate()    
    except: showerror('Error', 'Failed to close server')
    else: remove('apache/logs/httpd.pid')

def main_start():
    if path.isfile('main.pid') == False:
        try: mainpid = subprocess.Popen('python main.py').pid
        except: showerror('Error', 'Server failed to start.')
        else: pid_man('set', 'main', mainpid)
    else: showwarning('Warning', 'Server already running')

def main_stop():
    main = pid_man('get', 'main')
    mainproc = psutil.Process(main)
    try: mainproc.terminate()
    except: showerror('Error', 'Failed to close server')
    else: remove('main.pid')
   
def pid_man(task, program, pid=0):
    def get_pid(piddir):
        if path.isfile(piddir):
            pidfile = open(piddir, 'r')
            try: pid = int(pidfile.read()[0:-1])
            except: showwarning('Warning', 'Error reading pidfile. To close use Task Manager.')
            finally: pidfile.close()
            return pid
        else: return 0

    def set_pid(pid):
        pidfile = open('main.pid', 'w')
        try: pidfile.write(str(pid) + '\n')
        except: showwarning('Warning', 'Error writing pidfile. To close use Task Manager.')
        finally: pidfile.close()

    def check_pid(pidname):
        try:
            pidcheck = psutil.Process(pidname)
            if pidcheck.status == 0:
                return True
            else: return False
        except: return False
    
    if task == 'check': return check_pid(pid)
    elif task == 'get':
        if program == 'apache': return get_pid('../apache/logs/httpd.pid')
        elif program == 'main': return get_pid('main.pid')
    elif task == 'set' and program == 'main': set_pid(pid)

def browse_help():
    webbrowser.open('https://github.com/h1ll37/hillting/wiki')

frame = Frame()
startbutton = Button(frame)
stopbutton = Button(frame)
webstartbutton = Button(frame)
webstopbutton = Button(frame)
serverstatus = Label(frame)
webserverstatus = Label(frame)
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
startbutton.config(text='Start',command=main_start)
stopbutton.config(text='Stop',command=main_stop)
webstartbutton.config(text='Start',command=web_start)
webstopbutton.config(text='Stop',command=web_stop)

menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Quit', command=root.destroy)
menubar.add_cascade(label='Options', menu=optionsmenu)
menubar.add_command(label="Help", command=browse_help)

frame.pack()
seperator4.grid(column=0, row=0)
serverstatus.grid(column=0,row=1,rowspan=2, padx=15)
webserverstatus.grid(column=0,row=4,rowspan=2, padx=15)
startbutton.grid(column=2,row=1)
stopbutton.grid(column=2,row=2)
seperator.grid(column=2,row=3, padx=55, pady=5)
webstartbutton.grid(column=2,row=4)
webstopbutton.grid(column=2,row=5)
seperator2.grid(column=2,row=6, padx=55, pady=0)

root.mainloop()