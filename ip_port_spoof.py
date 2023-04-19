import socket

def check_port(host, port):
    spoofed_ip = '192.168.1.200'  # Cambiar por la IP falsificada que deseas utilizar
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((spoofed_ip, 0))
    sock.settimeout(1)
    result = sock.connect_ex((host, port))
    sock.close()
    if result == 0:
        print(f'El puerto {port} en el host {host} está abierto.')
    else:
        print(f'El puerto {port} en el host {host} está cerrado o no disponible.')

host = '192.168.1.100'  # Cambiar por la dirección IP del host que deseas escanear
port = 80  # Cambiar por el número de puerto que deseas verificar

check_port(host, port)
