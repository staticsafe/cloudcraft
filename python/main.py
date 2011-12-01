import subprocess
import os
import time
import socketserver
import socket

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

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((socket.gethostname(), 8080))
serversocket.listen(5)
conn, addr = serversocket.accept()
print('Connected by', addr)

while True:
    data = conn.recv
    if not data: break
    conn.send(data)
conn.close()
    
#while os.path.isfile('../web/php.lck') == True:
