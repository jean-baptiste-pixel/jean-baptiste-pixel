import socket

def get(url) -> object:
    ip = socket.gethostbyname(url)
    return ip