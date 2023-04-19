import scapy.all as scapy

# Crear paquete IP spoofing
spoofed_ip = "192.168.1.100"  # IP falsificada
target_ip = "192.168.1.1"  # IP de la víctima
packet = scapy.IP(src=spoofed_ip, dst=target_ip)
packet /= scapy.ICMP()  # Agregar capa ICMP

# Enviar paquete falsificado
scapy.send(packet, verbose=False)
