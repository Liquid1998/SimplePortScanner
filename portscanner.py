import socket
from IPy import IP

def scan(target):
    converted_ip = check_ip(target)
    print('\n' + '[^_^] Scanning Target.... ' + '  ' + str(target))
    for port in range(1,1000):
        scan_port(converted_ip, port)
        
def check_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)

def get_banner(s):
    return s.recv(1024)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            print('[+] Open Port ' + str(port) + '   ' + ' [+] Banner ' + ':' + str(banner.decode().strip('\n')))
        except:
            print('[+] Open Port ' + str(port))
    except:
        pass



if __name__ == "__main__":
    
    targets = input("[×] Enter Target/s To Scan (Split Target With ','): ")
    if ',' in targets:
        for ipadd in targets.split(','):
            scan(ipadd.strip(' '))
    else:
        scan(targets)