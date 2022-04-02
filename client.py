import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if len(sys.argv) > 1:
    host = sys.argv[1]
else:
    host = socket.gethostname()

port = 3003

s.connect((host,port))
print(f'Connection to the server - {host} Established! File ready to send')

#this will send the file once the server is rebooted.
file_to_send = open('collected_data.txt','rb')
l = file_to_send.read(1024)
while(l):
    s.send(l)
    l=file_to_send.read(1024)

s.close()
