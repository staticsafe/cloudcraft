from tkinter import *
from tkinter.ttk import *
from os import remove, path
import psutil
import subprocess
import socket

root = Tk()
root.title('Server Manager')
root.resizable(width=FALSE,height=FALSE)

def web_start():
	try: apachepid = subprocess.Popen('..\apache\bin\hw.exe httpd.exe')
	except: pass #open popup

def web_stop():
    apache = pid_man('apache', 'get')
    apacheproc = psutil.Process(apache)
    apacheproc.terminate()
    remove('apache\logs\httpd.pid')

def main_start():
    try: mainpid = subprocess.Popen('python main.py', stdin=subprocess.PIPE).pid
        pid_man('main', 'set', mainpid)
    except: pass #open popup
    
def main_stop():
    #if socket_comm('destroy') == False:
    main = pid_man('main', 'get')
    mainproc = psutil.Process(main)
    mainproc.terminate()
    remove('main.pid')

def mc_start(): pass
	# if socket_comm('start') == False:
	# 	#open popup
	# 	pass

def mc_stop(): pass
	# if socket_comm('stop') == False:
	# 	mc = pid_man('mc', 'get')
	# 	mc.terminate()
	# 	remove('mc.pid')

def pid_man(program, task, pid=0):
    def get_pid(piddir):
        if path.isfile(piddir):
            pidfile = open(piddir, 'r')
            pid = int(pidfile.read()[0:-1])
            pidfile.close()
            return pid
        else: return 0

    def set_pid(piddir, pidnum):
        pidfile = open(piddir, 'w')
        pidfile.write(str(pidnum) + '\n')
        pidfile.close()

    def check_pid(pidname):
        try:
            pidcheck = psutil.Process(pidname)
            if pidcheck.status == 0:
                return True
            else: return False
        except: return False
    
    if program == 'apache':
        if task == 'get': 
        	apache = get_pid('../apache/logs/httpd.pid')
        	return apache
        elif task == 'check': pass
    elif program == 'mc':
        if task == 'get': 
            mcpid = get_pid('mc.pid')
            return mcpid
        elif task == 'check': pass
    elif program == 'main':
        if task == 'get': 
            mainpid = get_pid('main.pid')
            return mainpid
        elif task == 'set': set_pid('main.pid', pid)
        elif task == 'check': pass
    else: pass

# def socket_comm(serverin):
#     serverin = serverin.encode('utf-8')
#     try:
#     	socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     	socket.connect(('localhost', 1337))
#     	socket.send(serverin)
#     	serverout = socket.recv(128)
#     	serverout = serverout.decode('utf-8')
#     	socket.close()
#     	return True
#     except: return False

# while True:
# 	if pid_man('apache', 'check') == False:
# 		asc.set('red')
# 	else: pass
	
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
startbutton.config(text='Start',command=main_start)
stopbutton.config(text='Stop',command=main_stop)
webstartbutton.config(text='Start',command=web_start)
webstopbutton.config(text='Stop',command=web_stop)
mcstartbutton.config(text='Start',command=mc_start)
mcstopbutton.config(text='Stop',command=mc_stop)

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
