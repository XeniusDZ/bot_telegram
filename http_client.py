import socket
import ssl
from urllib.parse import urlparse
import json


# request creates a socket client for connecting to a https server host and sends provided content.
# returns server response.
def request(host, content):
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_secure = ctx.wrap_socket(client)
    client_secure.connect((host, 443))

    client_secure.send(content.encode())

    response = ''
    while True:
        recv = client_secure.recv(1024)
        if not recv:
            break
        response += str(recv)

    client_secure.close()

    return response


# post sends a http post request with the values provided and authentication auth key if provided.
# returns response body
def post(url, values=None, auth=""):
    if values is None:
        values = []
    path = urlparse(url).path
    host = urlparse(url).hostname
    content_length = 0
    if values:
        content_length = len(json.dumps(values))
    body = 'POST ' + path + ' HTTP/1.1\r\nContent-Type: application/json\r\nConnection: close\r\nContent-Length: {}\r\nHost: '.format(
        content_length) + host
    if auth != '':
        body += '\r\nAuthorization: Bearer ' + auth

    body += '\r\n\r\n'

    if values:
        body += json.dumps(values)

    return request(host, body).split('\\r\\n\\r\\n', 1)[1][:-1]
