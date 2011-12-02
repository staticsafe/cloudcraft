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

def server_comm(serverin):
    if (serverin == 'start'):
        server_start()
    elif (serverin == 'terminate'):
        serverproc.terminate()
        os.remove('../minecraft/server.log.lck')
    else:
        serverproc.communicate(serverin)

command={'start':server_start(), 'terminate':serverproc.terminate()}

while True:
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind(('localhost', 1337))
    serversocket.listen(5)
    connection, address = serversocket.accept()
    while True:
        serverin = connection.recv(1024)
        if not serverin: break
        if serverin:
            serverin = serverin.decode('utf-8')
            server_comm(serverin)
            serverout = 'string\n'
            serverout = serverout.encode('utf-8')
        if serverout:
            connection.send(serverout)
    connection.close()
