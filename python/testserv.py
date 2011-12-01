import socket

host = 'localhost'
port = 1337              
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)
conn, addr = s.accept()
print('Connected by', addr)
while True:
    data = conn.recv(7)
    if not data: break
    conn.send(data)
conn.close()
