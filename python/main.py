import subprocess
import socket
from os import path, remove
from urllib.request import urlretrieve
from filecmp import cmp
from shutil import copy

def server_start(memory='1024M', jar='../minecraft/minecraft_server.jar', cwd='../minecraft/'):
    if path.isfile('../minecraft/server.log.lck'):
        return 'already running'
    else:
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = subprocess.SW_HIDE
        executable = 'java -Xmx' + memory + ' -Xms' + memory + ' -jar ' + jar + ' nogui'
        global serverproc
        serverproc = subprocess.Popen(executable, cwd=cwd, startupinfo=startupinfo, stdin=subprocess.PIPE, universal_newlines=True)
        
def server_comm(serverin):
    if (serverin == 'start'):
        server_start()
        return 'success'
    elif (serverin == 'terminate'):
        if serverproc:
            serverproc.terminate()
            remove(cwd +'server.log.lck')
            return 'success'
        if not serverproc:
            return 'failed'
        return 'success'
    elif (serverin == 'update'):
        if serverproc:
            pass
        if not serverproc:
            try:
                urlretrieve('https://s3.amazonaws.com/MinecraftDownload/launcher/minecraft_server.jar')
                if cmp('minecraft_server.jar', '../minecraft/minecraft_server.jar'):
                    remove('minecraft_server.jar')
                else:
                    remove('../minecraft/minecraft_server.jar')
                    copy('minecraft_server.jar', '../minecraft/minecraft_server.jar')
                    remove('minecraft_server.jar')
                    return 'success'
            except: pass
    else:
        try:
            serverproc.communicate(serverin)
            return 'success'
        except NameError as error:
            return 'failed'
    
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
