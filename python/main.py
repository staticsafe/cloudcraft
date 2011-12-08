import subprocess
import socket
import zipfile
import configparser
import psutil  # http://code.google.com/p/psutil/
from os import path, remove, rename, name
from urllib.request import urlretrieve
from filecmp import cmp
from time import wait

def server_start():
    update_config()
    if pid_man() == True:
        return 'Already running'
    else:
        if (name == 'posix' or 'mac'):
            startupinfo = None
        if (name == 'nt'):
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            startupinfo.wShowWindow = subprocess.SW_HIDE
        executable = 'java -Xmx' + memory + ' -jar ' + mcdir + jar + ' nogui'
        global serverproc
        serverproc = subprocess.Popen(executable, cwd=mcdir, startupinfo=startupinfo, stdin=subprocess.PIPE, universal_newlines=True)
        newpid = serverproc.pid
        pid_man(newpid)
        
def server_comm(serverin):
    if (serverin == 'start'):
        server_start()
        return 'Starting'
    elif (serverin == 'terminate'):
        if pid_man():
            oldpid.terminate()
            remove(mcdir +'server.log.lck')
            return 'Terminated'
        if pidman() == False:
            return 'Server not running'
    elif (serverin == 'update'):
        update_config()
        if (jar == 'minecraft_server.jar'):
            try:
                newjar = urlretrieve('https://s3.amazonaws.com/MinecraftDownload/launcher/minecraft_server.jar')
                try:
                    if cmp(newjar[0], jar):
                        return 'No update available'
                    else:
                        try:
                            serverproc.comm("server going down for update")
                            wait(15)
                            serverproc.comm(stop)
                            remove(mcdir + jar)
                            rename(newjar[0], mcdir + jar)
                            return 'Updated'
                        except: return 'copy failed, try killing server'
                except:rename(newjar[0], mcdir + jar)
            except: return 'minecraft.net down'
        else: return 'bukkit support coming'
    else:
        try:
            serverproc.communicate(input=serverin)
            return 'Sent'
        except NameError:
            try:
                if pid_man() == True:
                    return 'Lost communication to server, try killing'
                else:
                    return 'Server not running'

def update_config():    
    config = configparser.ConfigParser()
    config.read('config.ini')
    mcargs = config['mcargs']
    global mcdir
    global jar
    global backupdir
    global memory
    mcdir = mcargs['mcdir']
    jar = mcargs['jar']
    backupdir = mcargs['backupdir']
    memory = mcargs['memory']

def pid_man(newpid=0):
    if newpid != 0:
        try:
            remove('pid')
        except: pass
        pidfile = open('pid', 'w')
        pidfile.write(newpid)
        pidfile.close()
    if newpid == 0:
        pidfile = open('pid', 'r')
        global oldpid
        oldpid = int(pidfile.read())
        pidfile.close()
        try:
            pidcheck = psutil.Process(oldpid)
            if (pidcheck.status) == 0:
                return True
            else: return False
        except: return False
    
update_config()

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 1337))
serversocket.listen(5)
while True:
    connection, address = serversocket.accept()
    while True:
        serverin = connection.recv(128)
        if not serverin: break
        if serverin:
            serverin = serverin.decode('utf-8')
            serverout = server_comm(serverin)
        if not serverout: break
        if serverout:
            try:
                serverout = serverout + '\n'
                serverout = serverout.encode('utf-8')
                connection.send(serverout)
            except OSError as error: pass
