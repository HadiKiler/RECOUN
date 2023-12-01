import socket
from concurrent.futures import ThreadPoolExecutor
execute = ThreadPoolExecutor()

def get_ports(ip):
    ports = []
    common_ports = [21, 22, 23, 25, 53, 80, 110, 119, 123, 143, 161, 194, 443, 445, 993, 995]
    tasks = [execute.submit(a, ip, port) for port in common_ports]
    for task in tasks:
        result = task.result()
        if result != None:
            ports.append(result)
    return ports



def a(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # Set timeout to 1 second
    result = sock.connect_ex((ip, port))
    if result == 0:
        return port
    sock.close()



