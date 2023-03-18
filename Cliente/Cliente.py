import socket

#Envia o nome do arquivo para o Servidor
filename = input("Digite o nome do arquivo com a extensão .txt que deseja enviar para o servidor: ")

# Cria um objeto socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta-se ao servidor
server_address = ('localhost', 8000)
client_socket.connect(server_address)

# Envia o nome do arquivo para o servidor
client_socket.send(filename.encode())

# Recebe o conteúdo do arquivo enviado pelo servidor
conteudo_arquivo = client_socket.recv(1024).decode()

# Salva o conteúdo em Arquivo.txt
with open("Arquivo.txt", 'w') as arquivo_local:
    arquivo_local.write(conteudo_arquivo)

# Fecha o socket
client_socket.close()

