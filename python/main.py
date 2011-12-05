import subprocess
import socket
import zipfile
import configparser
from os import path, remove, rename, name
from urllib.request import urlretrieve
from filecmp import cmp

def server_start():
    update_config()
    if path.isfile(mcdir + 'server.log.lck'):
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
        
def server_comm(serverin):
    if (serverin == 'start'):
        server_start()
        return 'Started'
    elif (serverin == 'terminate'):
        if serverproc:
            serverproc.terminate()
            remove(mcdir +'server.log.lck')
            return 'Terminated'
        if not serverproc:
            return 'Server not running'
    elif (serverin == 'backup'):	
        backupfile = zipfile.ZipFile(backupdir + 'world.zip', mode='w', compression=zipfile.ZIP_DEFLATED)
        world = open('../minecraft/world/')
        backupfile.write(world)
        backupfile.close()
        world.close()
        return 'Backed Up'
    elif (serverin == 'update'):
        update_config()
        try:
            if (jar == 'minecraft_server.jar'):
                newjar = urlretrieve('https://s3.amazonaws.com/MinecraftDownload/launcher/minecraft_server.jar')
                if cmp(newjar[0], jar):
                    return 'No update available'
                else:
                    try:
                        serverproc.comm(stop)
                    remove(mcdir + jar)
                    rename(newjar[0], mcdir + jar)
                    return 'Updated'
            else: return 'bukkit support coming'
        except: return 'minecraft.net down'
    else:
        try:
            serverproc.communicate(input=serverin)
            return 'Sent'
        except NameError as error:
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
