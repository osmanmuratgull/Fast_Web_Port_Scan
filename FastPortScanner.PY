import socket
import concurrent.futures

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)  # You can set the timeout period
        result = sock.connect_ex((target, port))
        if result == 0:
            return port
    except socket.error:
        pass
    return None

def scan_ports(target, start_port, end_port):
    open_ports = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        port_range = range(start_port, end_port + 1)
        results = executor.map(lambda port: scan_port(target, port), port_range)
        for port, result in zip(port_range, results):
            if result is not None:
                open_ports.append(result)
                print(f"Port {port} açık")
            else:
                print(f"Port {port} kapalı")
    return open_ports

target_ip = "127.0.0.1"  # Enter the destination IP address here
start_port = 1  # Enter here the port number from which the scan will start
end_port = 65535  # Enter the port number where the scan will end here

open_ports = scan_ports(target_ip, start_port, end_port)

if open_ports:
    print("Açık portlar:")
    for port in open_ports:
        print(port)
else:
    print("Açık port bulunamadı.")
