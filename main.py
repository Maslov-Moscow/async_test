import socket

from mods import *


def main():
    mods = {
        '1': single_request,
        '2': connection,
        '3': event_loop
    }

    mod = input('Choose mode:\n1.Single request\n2.Connection\n3.Event loop\n')
    if mod not in mods:
        raise Exception('Wrong choose!')

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()
    print(f'Server ready accept connection. Mode {mod}')

    mods[mod](server_socket)


if __name__ == '__main__':
    main()
