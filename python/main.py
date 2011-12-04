import subprocess
import socket
import zipfile
import configparser
from os import path, remove, rename, name
from urllib.request import urlretrieve
from filecmp import cmp

update_config()

def server_start():
    if isfile(mcdir + 'server.log.lck'):
        return 'Already running'
    else:
        if (os.name == 'nt'):
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            startupinfo.wShowWindow = subprocess.SW_HIDE
        if (os.name == 'posix' or 'mac'):
            startupinfo = None
        update_config()
        executable = 'java -Xmx' + memory + ' -jar ' + mcdir + jar + ' nogui'
        global serverproc
        serverproc = subprocess.Popen(executable, mcdir=mcdir, startupinfo=startupinfo, stdin=subprocess.PIPE, universal_newlines=True)
        return 'Running'
    
def server_comm(serverin):
    if (serverin == 'start'):
        server_start()
    elif (serverin == 'terminate'):
        if serverproc:
            serverproc.terminate()
            remove(mcdir +'server.log.lck')
            return 'Terminated'
        if not serverproc:
            return 'Server not running'
    elif (serverin == 'backup'):
        if serverproc:
            return 'Please close before backing up'
        if not serverproc:
            update_config()
            try:
                currentmap = file.open(mcdir + '/world/')
                backupfile = zipfile.ZipFile(backupdir + 'world.zip', mode='w', compression=ZIP_DEFLATED)
                file.write(currentmap)
                file.close()
            except: return 'Backup Failed'              
    elif (serverin == 'update'):
        if serverproc:
            return 'Please close before updating'
        if not serverproc:
            update_config()
            try:
                if (jar == 'minecraft_server.jar'):
                    newjar = urlretrieve('https://s3.amazonaws.com/MinecraftDownload/launcher/minecraft_server.jar')
                    if cmp(newjar[0], jar):
                        return 'No update available'
                    else:
                        remove(mcdir + jar)
                        rename(newjar[0], mcdir + jar)
                        return 'Updated'
                else: pass
            except: return 'minecraft.net down'
    else:
        try:
            serverproc.communicate(serverin)
            return 'sent'
        except NameError as error:
            return 'Server not running'

def update_config():    
    config = configparser.ConfigParser()
    config.read('config.ini')
    mcargs = config['mcargs']
    mcdir = mcargs['mcdir']
    jar = mcargs['jar']
    backupdir = ['backupdir']
    memory = ['memory']
    
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
