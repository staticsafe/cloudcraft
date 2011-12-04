import socket
import time

HOST = 'localhost'  
PORT = 1337              
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send(b'start')
print('sent start')
msg = s.recv(128)
print(msg)
s.close()
print('waiting')
time.sleep(10)
print('waited')
s.connect((HOST, PORT))
s.send(b'whitelist add TingPing')
print('sent stop')
msg = s.recv(128)
print(msg)
s.close()
print('waiting')
time.sleep(5)
print('waited')
s.connect((HOST, PORT))
s.send(b'stop')
print('sent stop')
msg = s.recv(128)
print(msg)
s.close()



