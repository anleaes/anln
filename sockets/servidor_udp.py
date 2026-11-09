import socket

soquete = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    mensagem = input()
    soquete.sendto(mensagem.encode(),("192.168.1.10",8000)) 