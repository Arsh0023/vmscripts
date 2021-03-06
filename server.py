import socket
from datetime import date

#This will recieve the file once connection is made.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '0.0.0.0'
port = 3003
s.bind((host,port))
s.listen(5)
print(f'Waiting for incoming connections on port {port}')

conn , addr = s.accept()
file = open(f'collected_data_{date.today()}.txt','wb')

with conn:
    print(f'Connected by {addr}')
    while True:
        data = conn.recv(1024)
        if not data:
            break
        file.write(data)
        
file.close()
s.close()
