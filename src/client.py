#!/usr/bin/env python3

from sys import argv

import Pyro5.api
import Pyro5.errors

class Client():
    def configure_client():
        if len(argv) < 2:
            print('Nome do arquivo: <file>')
            print('Nome do servidor: <server_name>')
            print('Mensagem: <message>')
            print('\nExemplo: python3 <file>.py <server_name> <message>\n')
            exit(1)

        name = argv[1]

        # get reference to obj.
        ref = Pyro5.api.Proxy('PYRONAME:' + name)

        return ref

    def get_client_message_argv():
        message = argv[2]
        return message

if __name__ == '__main__':
    eco = Client.configure_client()

    try:
        print('Chamando operação...', flush=True)
        message = Client.get_client_message_argv()

        print('response =', eco.send(message))
        print('counter =', eco.get_counter(), end='\n\n')

    except Pyro5.errors.CommunicationError as e:
        print('Crash failure detected')
        print(e)
    except Pyro5.errors.NamingError as ne:
        print('Name not found on name server')
        print(ne)
