import subprocess
import os
import time

def server_start(memory='1024M', jar='../minecraft/minecraft_server.jar'):
    if os.path.isfile('../minecraft/server.log.lck'):
        return 'Already Running'
    else:
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = subprocess.SW_HIDE
        executable = 'java -Xmx' + memory + ' -Xms' + memory + ' -jar ' + jar + ' nogui'
        global serverproc
        serverproc = subprocess.Popen(executable, startupinfo=startupinfo, stdin=subprocess.PIPE, universal_newlines=True)
        return 'Started'

def server_comm(serverin):
    if (serverin == 'start'):
        server_start()
        return 'Started'
    elif (serverin == 'terminate'):
        global serverproc
        serverproc.terminate()
        os.remove('../minecraft/server.log.lck')
        return 'terminated'
    elif serverin == 'list':
        pass
    else:
        global serverproc
        serverproc.communicate(serverin)
        return 'Sent'

while True:
    time.sleep(10)
    while os.path.isfile('../php.lck'):
        file = open('communicate')
        global serverin
        serverin = file.readline()
        file.close()
        server_comm(serverin)
        os.remove('communicate')
        time.sleep(3)
