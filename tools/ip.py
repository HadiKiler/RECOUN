import socket

def get_ip(domain):
    return socket.gethostbyname(domain)