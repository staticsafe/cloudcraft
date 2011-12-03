import subprocess
import socket
from os import path, remove, rename
from urllib.request import urlretrieve
from filecmp import cmp

def server_start(memory='1024M', jar='../minecraft/minecraft_server.jar', cwd='../minecraft/'):
    if serverproc:
        return 'already running'
    else:
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = subprocess.SW_HIDE
        executable = 'java -Xmx' + memory + ' -Xms' + memory + ' -jar ' + jar + ' nogui'
        global serverproc
        serverproc = subprocess.Popen(executable, cwd=cwd, startupinfo=startupinfo, stdin=subprocess.PIPE, universal_newlines=True)
        return 'Running'
def server_comm(serverin):
    if (serverin == 'start'):
        server_start()
    elif (serverin == 'terminate'):
        if serverproc:
            serverproc.terminate()
            remove(cwd +'server.log.lck')
            return 'Terminated'
        if not serverproc:
            return 'Server not running'
    elif (serverin == 'update'):
        if serverproc:
            return 'Please close before updating'
        if not serverproc:
            try:
                newjar = urlretrieve('https://s3.amazonaws.com/MinecraftDownload/launcher/minecraft_server.jar')
                if cmp(newjar[0], jar):
                    return 'No updated available'
                else:
                    remove('../minecraft/minecraft_server.jar')
                    rename(newjar[0], '../minecraft/minecraft_server.jar')
                    return 'Updated'
            except: return 'minecraft.net down'
    else:
        try:
            serverproc.communicate(serverin)
            return 'sent'
        except NameError as error:
            return 'Server not running'
    
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
