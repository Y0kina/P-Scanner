import socket
import sys
from datetime import datetime


def scan_port(target, port):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((target, port))

    if result == 0:
        try:
            sock.send(b"Hello\r\n")
            banner = sock.recv(1024).decode().strip()
        except Exception:
            banner = "No banner available"

        sock.close()
        return True, banner
    else:
        sock.close()
        return False, None


def scan_range(target, start_port, end_port):

    open_ports = []

    print(f"\nStarting scan on {target} — {datetime.now()}")
    print(f"Ports tested: {start_port} to {end_port}\n")

    for port in range(start_port, end_port + 1):
        is_open, banner = scan_port(target, port)

        if is_open:
            print(f"[+] Port {port} OPEN — {banner}")
            open_ports.append((port, banner))

    return open_ports


def save_results(target, open_ports, file_name="scan_results.txt"):

    with open(file_name, "w") as f:
        f.write(f"Scan results for {target}\n")
        f.write(f"Date: {datetime.now()}\n")
        f.write("-" * 40 + "\n")

        if not open_ports:
            f.write("No open ports found.\n")
        else:
            for port, banner in open_ports:
                f.write(f"Port {port} — {banner}\n")

    print(f"\nResults saved to '{file_name}'")


def main():
    target = input("IP address or hostname to scan (e.g. 127.0.0.1): ")
    start_port = int(input("Start port: "))
    end_port = int(input("End port: "))

    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("Error: could not resolve this address.")
        sys.exit()

    open_ports = scan_range(ip, start_port, end_port)

    print(f"\nScan complete. {len(open_ports)} open port(s) found.")

    save_results(ip, open_ports)


if __name__ == "__main__":
    main()
