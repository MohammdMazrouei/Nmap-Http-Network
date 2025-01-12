import socket
import sys


def check_port_range(host: str, start_port: int, end_port: int) -> dict:
    open_ports = {}
    for port in range(start_port, end_port + 1):
        service = check_port(host, port)
        if service:
            open_ports[port] = service 

    return open_ports


def check_port(host: str, port: int) -> str:
    service = ""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((host, port))
        service = socket.getservbyport(port)
        s.close()

    except:
       return service

    return service 


def main():
    host = sys.argv[1]

    # check port common ports for host is online
    common_ports = [80, 443, 20, 21, 22, 25, 53, 123]
    for port in common_ports:
        if check_port(host, port):
            print(f'{host} is online')
            break
    else:
        print(f'{host} is offline')

    if (len(sys.argv) > 2):
        print('open ports detected:')
    for i in range(2, len(sys.argv)):

        port = sys.argv[i]
        open_ports = dict()

        if '-' in port:
            start_port, end_port = map(int, port.split('-'))
            open_ports = check_port_range(host, start_port, end_port)
        else:
            service = check_port(host, int(port))
            if service:
                open_ports[port] = service

        for port, service in open_ports.items():
            print(f'Port: {port}\tService: {service}')


if __name__ == '__main__':
    main()

