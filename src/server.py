#!/usr/bin/env python3

import math
import signal
from sys import argv

import Pyro5.api

MAX_MESSAGES = 3  # ve
MAX_TIMEOUT = 5  # to

@Pyro5.api.expose
class Eco(object):
    def __init__(self, max_messages: int = MAX_MESSAGES):
        self.counter = 0
        self.messages = []
        self.max_messages = max_messages

    def send(self, message):
        if self.messages == []:
            self.counter = 0
            self.messages.append(message)
            self.counter = self.counter + 1
            
            signal.alarm(MAX_TIMEOUT)
            return 'Mensagem entregue!'
        else:
            self.messages.append(message)
            self.counter = self.counter + 1

            if len(self.messages) == self.max_messages:
                print(self.voter())

            return 'Mensagem entregue!'

    def voter(self):
        signal.alarm(0)
        received_messages = self.messages.copy() # vr
        self.messages = []

        majority = math.ceil((self.max_messages + 1) / 2)
        
        if len(received_messages) >= majority:
            for msg in received_messages[:majority]:
                if received_messages.count(msg) >= majority:
                    return f'Veredito = {msg}\n'

        return 'Veredito = Inconclusivo\n'

    def get_counter(self):
        return self.counter

    def timeout(self, signum, pilha):
        print('Timeout acabou!')
        print(self.voter())

class Server():
    @staticmethod
    def get_server_argvs():
        if len(argv) < 2:
            print('Nome do servidor: <nome>')
            exit(1)
        else:
            name = argv[1]
            return name

    @staticmethod
    def configure_server(server_name: str):
        eco = Eco()                                 # instancia servant
        uri = daemon.register(eco)                  # registra pyro obj.
        signal.signal(signal.SIGALRM, eco.timeout)  # alarme com callback
        print('URI =', uri)                         # publica a URI
        ns = Pyro5.api.locate_ns()                  # name server
        ns.register(server_name, uri)               # registra referência no name server


if __name__ == '__main__':
    # obtendo nome do server
    name = Server.get_server_argvs()

    # daemon Pyro
    daemon = Pyro5.api.Daemon()
    Server.configure_server(name)

    print(f'"{name}" Aguardando requisições...\n')
    
    # inicia loop de espera
    daemon.requestLoop()

