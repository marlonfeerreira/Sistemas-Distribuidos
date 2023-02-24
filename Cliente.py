import socket
from random import randint

HOST = 'localhost'
PORT = 50000

# ipv4 e TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))

for valor in range(0, 1000):

    n = valor
    n = n-1+(randint(1,100))

    s.sendall(str.encode(str(n)))

    dados = s.recv(160)

    print("mensagem enviada de volta :", dados.decode())
    