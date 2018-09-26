#Adding IP Address to cmd
#Courtesy: StackOverflow.com
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org',80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.1\r\nHost: 2405:204:f208:a2d4:299d:287e:f857:d1cf\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if(len(data) < 1):
        break
    print(data.decode())
mysock.close()
