#!/usr/bin/env python3.9

#Importando o módulo socket
from socket import *
from time import sleep

#Criando as variáveis que armazenam a porta e o IP do servidor
serverName = '127.0.0.1'
serverPort = 12000
print('Variáveis serverName e serverPort criadas')
sleep(5)

#Criando o socket SOCK_STREAM é o protocolo TCP
print('Criando o socket...')
sleep(5)
clientSocket = socket(AF_INET, SOCK_STREAM)
print('Socket criado')

#Em TCP precisamos criar um handshake para começar a conexão, para isso usaremoso socket de como 'Boas vindas' iniciando a conexão com o atributo dele chamdo connect() e depois faremos o processo de envio dos dados, é como se tivesse um túnel entre eles.
clientSocket.connect((serverName, serverPort))
print('Conectando ao servidor...')
sleep(5)
print('Conexão funcionando!')

#'msg' significa mensagem
msg = str(input('Digite a frase que o servidor vai processar e transformar em MAIUSCULA: '))

#Envia a mensagem
clientSocket.send(msg.encode())
print('Enviado a msg para o servidor')
sleep(10)

# Recebe a mensagem capitalizada
msgUpper = clientSocket.recv(2048)
print('Recebendo a mensagem capitalizada... ')
sleep(5)

# Printa a mensagem capitalizada
print('Essa é a frase capitalizada: {}'.format(msgUpper.decode()))

# Fecha a conexão
print('Fechando a conexão...')
sleep(5)
clientSocket.close()
