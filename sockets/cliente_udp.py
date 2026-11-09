import socket      

soquete = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

soquete.bind(("192.168.1.10", 8000))

while True:
    print(soquete.recvfrom(1024))