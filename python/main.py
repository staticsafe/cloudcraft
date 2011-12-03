import subprocess
import os
import socket
#import threading

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
        print('started')
        return serverproc
        
def server_comm(serverin):
    if (serverin == 'start'):
        server_start()
        return 'works'
    elif (serverin == 'terminate'):
        serverproc.terminate()
        os.remove('../minecraft/server.log.lck')
        return 'killed'
    else:
        try:
            serverproc.communicate(serverin)
            return 'sent'
        except NameError as error:
            return 'Server not running'

#command={'start':server_start(), 'terminate':serverproc.terminate()}


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind(('localhost', 1337))
serversocket.listen(5)
print('listening')
while True:
    connection, address = serversocket.accept()
    print('connected by ', address)
    while True:
        serverin = connection.recv(128)
        if not serverin: break
        if serverin:
            serverin = serverin.decode('utf-8')
            print(serverin)
            serverout = server_comm(serverin)
        if not serverout: break
        if serverout:
            try:
                serverout = serverout + '\n'
                print(serverout)
                serverout = serverout.encode('utf-8')
                connection.send(serverout)
            except OSError as error:
                print(error)
                pass
