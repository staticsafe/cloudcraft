import subprocess
import os
import socket

def server_start(memory='1024M', jar='../minecraft/minecraft_server.jar', cwd='../minecraft/'):
    if os.path.isfile('../minecraft/server.log.lck'):
        return 'already running'
    else:
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = subprocess.SW_HIDE
        executable = 'java -Xmx' + memory + ' -Xms' + memory + ' -jar ' + jar + ' nogui'
        global serverproc
        serverproc = subprocess.Popen(executable, cwd=cwd, startupinfo=startupinfo, stdin=subprocess.PIPE, universal_newlines=True)
        global returncode
        returncode = serverproc.returncode
        
def server_comm(serverin):
    if (serverin == 'start'):
        server_start()
        return 'started'
    elif (serverin == 'terminate'):
        serverproc.terminate()
        os.remove('../minecraft/server.log.lck')
        return 'killed'
    else:
        serverproc.communicate(serverin)
        return 'sent'

#command={'start':server_start(), 'terminate':serverproc.terminate()}

while True:
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind(('localhost', 1337))
    serversocket.listen(5)
    connection, address = serversocket.accept()
    while True:
        serverin = connection.recv(128)
        if not serverin: break
        if serverin:
            serverin = serverin.decode('utf-8')
            serverout = server_comm(serverin)
        if serverout:
            try:
                serverout = serverout.encode('utf-8')
                connection.send(serverout)
            except:
                break
    connection.close()
