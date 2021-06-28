import socket

from services import *


def main():

    mode = input('Choose mode:\n1.Single request\n2.Connection\n')
    if mode != '1' and mode != '2':
        raise Exception('Wrong choose!')


    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()
    print(f'Server ready accept connection. Mode {mode}')
    if mode == '1':
        while True:
            client_socket, adrr = server_socket.accept()
            print(f'Connection from {adrr[0]}:{adrr[1]}')

            request = client_socket.recv(1024)
            print('Receive request')

            response = generate_response(request.decode('utf-8'))
            client_socket.send(response)
            print(f'Send response to {adrr[0]}:{adrr[1]}')

            client_socket.close()
            print('Connection close\n\n')
    elif mode == '2':
        while True:
            client_socket, adrr = server_socket.accept()
            print(f'Connection from {adrr[0]}:{adrr[1]}')

            while True:
                request = client_socket.recv(1024)
                print(f'Receive request:{request.decode("utf-8")}')

                if not request:
                    break
                else:
                    response = 'Hello world\n'.encode()
                    client_socket.send(response)
            client_socket.close()
            print('Connection close\n\n')



if __name__ == '__main__':
    main()
