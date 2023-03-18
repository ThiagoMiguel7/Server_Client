import socket

print("Server Ready")

# Cria um objeto socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define o endereço IP e a porta do servidor
server_address = ('localhost', 8000)
server_socket.bind(server_address)

# Aguarda por uma conexão
server_socket.listen(1)

# Aceita a conexão
client_socket, client_address = server_socket.accept()

# Recebe o nome do arquivo enviado pelo cliente
filename = client_socket.recv(1024).decode()

with open(filename, 'r') as arquivo:
    conteudo_arquivo = arquivo.read()

# Envia o conteúdo do arquivo para o cliente
client_socket.send(conteudo_arquivo.encode())
