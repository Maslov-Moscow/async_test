URLS = {
    '/': 'Index',
    '/test': 'Test'
}

to_monitor = []


def parse_request(request):
    parsed = request.split(' ')
    return parsed[0], parsed[1]


def generate_headers(method, url):
    if not method == 'GET':
        return ('HTTP/1.1 405 Method not allowed\n\n', 405)

    if not url in URLS:
        return ('HTTP/1.1 404 Not found\n\n', 404)

    return ('HTTP/1.1 200 OK\n\n', 200)


def generate_content(code, url):
    if code == 404:
        return '<h1>404</h1><p>Not found</p>'
    if code == 405:
        return '<h1>405</h1><p>Method not allowed</p>'
    return f'<h1>{URLS[url]}</h1>'


def generate_response(request):
    method, url = parse_request(request)
    headers, code = generate_headers(method, url)
    body = generate_content(code, url)
    return (headers + body).encode()


def accept_connection(server_socket):
    client_socket, adrr = server_socket.accept()
    print(f'Connection from {adrr[0]}:{adrr[1]}')

    to_monitor.append(client_socket)


def send_message(client_socket):
    request = client_socket.recv(1024)
    print(f'Receive request:{request.decode("utf-8")}')

    if request:
        response = 'Hello world\n'.encode()
        client_socket.send(response)
    else:
        to_monitor.remove(client_socket)
        client_socket.close()
        print('Connection close\n\n')
