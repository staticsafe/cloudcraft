import subprocess
import os
import time

def server_start(memory='1024M', jar='../minecraft/minecraft_server.jar', cwd='../minecraft/'):
    if os.path.isfile('../minecraft/server.log.lck'):
        pass
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
    elif (serverin == 'terminate'):
        serverproc.terminate()
        os.remove('../minecraft/server.log.lck')
    else:
        serverproc.communicate(serverin)

while True:
    time.sleep(10)
    while os.path.isfile('../web/php.lck'):
        if os.path.isfile('communicate'):
            file = open('communicate')
            serverin = file.readline()
            file.close()
            server_comm(serverin)
            os.remove('communicate')
        else:
            time.sleep(3)
