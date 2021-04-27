#!/usr/bin/env python3.9

#Importando o módulo socket e o módulo time
from socket import *
from time import sleep

#Atribuir a porta ao servidor e criar o socket
serverPort = 12000
print('Esse servidor usará a porta {} para conexão'.format(serverPort))
sleep(5)
print('Criando o socket que utilizarei para essa aplicação...')
serverSocket = socket(AF_INET, SOCK_STREAM)
sleep(10)

#Atribuir um IP e uma porta ao socket '' significa que o kernel vai atribuir o IP para nós (Vai utilizar o IP local se testar na mesma máquina) 
print('Amarrando o meu endereço de IP e a porta para o socket que acabei de criar...')
serverSocket.bind(('', serverPort))
sleep(10)

print('Estou pronto e esperando conexões...')
print('Já pode abrir o arquivo TCPClient.py')
# O servidor está esperando pela conexão, esse .listen(1) escuta e 1 é o numero máximo de conexões em fila'
serverSocket.listen(1)

#Após a escuta ele vai entrar num loop infinito, há maneiras de interromper esse lopp, mas nesse caso eu vou deixar infinito.
while True:
    # OBS: TEMOS UMA PARTICULARIDADE AQUI (TCP), NOSSO SOCKET serverSocket É APENAS UMA ENTRADA PARA A CONEXÃO, ELE QUE FAZ O HANDSHAKE;
    # connectionSocket e addr vão herdar os parâmetros que o método .accept() passar para eles respectivamente (ler a documentação)
    # Quando o cliente bate na porta '.listen()' ele passa direto para esse looping que cria uma conexão somente para o cliente que está tentando conectar, é assim que conseguimos várias conexões no servidor TCP.
    connectionSocket, addr = serverSocket.accept()
    print('Criei o Socket temporário que vou usar para falar com o cliente: {}, esse é o socket que usaremos para trocar informações'.format(addr))
    # Aqui funciona como o outro código
    msg = connectionSocket.recv(1024)
    print('Recebi o pacote...')
    sleep(5)
    msg = msg.decode()
    print('Decodifiquei o pacote...')
    sleep(5)
    msg = msg.upper()
    print('Transfomei a mensagme em upper case...')
    sleep(5)
    print('Me preparando para enviar a mensagem...')
    sleep(10)
    connectionSocket.send(msg.encode())
    print('Mensagem ENVIADA!!')

    #fecha a conexão
    connectionSocket.close()
