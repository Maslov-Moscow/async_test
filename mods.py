from select import select

from services import *


def single_request(server_socket):
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


def connection(server_socket):
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


def event_loop(server_socket):
    to_monitor.append(server_socket)
    while True:
        ready_to_read, _, _ = select(to_monitor, [], [])

        for sock in ready_to_read:
            if sock is server_socket:
                accept_connection(sock)
            else:
                send_message(sock)
