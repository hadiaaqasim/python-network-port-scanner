import socket
from datetime import datetime

# Take input from user
target = input("Enter target IP address or hostname: ")
start_port = int(input("Enter starting port: "))
end_port = int(input("Enter ending port: "))

# Convert hostname to IP address
try:
    target_ip = socket.gethostbyname(target)

except socket.gaierror:
    print("Error: Invalid hostname or IP address.")
    exit()

# Common service names
common_services = {
    20: "FTP Data",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP"
}

# Display scan information
print("\n" + "-" * 50)
print(f"Scanning Target: {target}")
print(f"IP Address: {target_ip}")
print(f"Port Range: {start_port} - {end_port}")
print(f"Scan Started At: {datetime.now()}")
print("-" * 50)

try:
    # Scan each port in the given range
    for port in range(start_port, end_port + 1):

        # Create a socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Set timeout (1 second)
        sock.settimeout(1)

        # Attempt connection
        result = sock.connect_ex((target_ip, port))

        # If connection successful
        if result == 0:
            service = common_services.get(port, "Unknown Service")
            print(f"[OPEN] Port {port} - {service}")

        # Close the socket
        sock.close()

except KeyboardInterrupt:
    print("\nScan interrupted by user.")

except socket.error:
    print("\nNetwork error occurred.")

print("\nScan Completed.")