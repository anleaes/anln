import socket
import threading
import os

soquete = socket.socket(socket.AF_INET , socket.SOCK_DGRAM )
soquete.bind(("192.168.1.10", 8000))

print("  ----------  ")
print(" | CHAT UDP | ")
print("  ----------  ")

nome = input("\nDigite seu nome: ")

print("\nDigite 'sair' para encerrar a sessao.")

def send():
    while True:
        mensagem = input()
        if mensagem == "sair":
            os._exit(1)
        envio_mensagem = "{}: {}".format(nome, mensagem)
        soquete.sendto(envio_mensagem.encode(), ("192.168.1.11", 8001))

def rec():
    while True:
        recebe_mensagem = soquete.recvfrom(1024)
        print(" " +  recebe_mensagem[0].decode() )

maquina1 = threading.Thread(target = send)
maquina2 = threading.Thread(target = rec)

maquina1.start()
maquina2.start()