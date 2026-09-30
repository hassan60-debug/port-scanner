import socket
import datetime

# Common ports and their services
COMMON_SERVICES = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
    53: "DNS", 80: "HTTP", 110: "POP3", 143: "IMAP",
    443: "HTTPS", 445: "SMB", 3306: "MySQL", 3389: "RDP",
    8080: "HTTP-Alt", 8443: "HTTPS-Alt"
}

def scan_ports(target, start_port, end_port):
    print(f"\n{'='*50}")
    print(f"  Network Port Scanner")
    print(f"  Target : {target}")
    print(f"  Time   : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*50}\n")

    open_ports = []

    try:
        target_ip = socket.gethostbyname(target)
        print(f"  Resolved IP: {target_ip}\n")
    except socket.gaierror:
        print("  Error: Hostname could not be resolved.")
        return

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            service = COMMON_SERVICES.get(port, "Unknown")
            print(f"  [OPEN] Port {port:5d}  →  {service}")
            open_ports.append(port)
        sock.close()

    print(f"\n{'='*50}")
    print(f"  Scan complete — {len(open_ports)} open port(s) found")
    print(f"{'='*50}\n")

# Run
target = input("Enter target (e.g. scanme.nmap.org): ")
start  = int(input("Start port: "))
end    = int(input("End port: "))
scan_ports(target, start, end)