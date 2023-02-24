import socket

HOST = 'localhost'
PORT = 50000

# ipv4 e TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))

s.listen()
print("Aguardando conexão do cliente")

conn, ender = s.accept()

print('Conectado em',  ender)


while True:
    # 160 bits = 20 bytes
    dados = conn.recv(160)


    if not dados:
        print("Fechando conexão")
        conn.close()
        break

    # verificando se é primo
    numero = int(dados)

    if numero > 1:
        for i in range(2, numero):
            if numero % i == 0:
                dados += b' nao e primo'
                break
        else:
            dados += b' e primo'
    elif numero == 0:
        dados += b' e zero'
    elif numero == 1:
        dados += b' e um'
    else:
        dados += b' e negativo'
    
    conn.sendall(dados)
