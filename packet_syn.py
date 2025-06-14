from scapy.all import *
from scapy.layers.inet import IP, TCP, sr1

packet = IP(dst="scanme.nmap.org") / TCP(dport = 80, flags='S')

response = sr1(packet, timeout=2)

if response:
    response.show()

    resp_ip = response[IP]

    # Check if SYN-ACK
    if response.haslayer(TCP) and response[TCP].flags == "SA":
        print("✅ Port 80 is OPEN (SYN-ACK received)")
    elif response.haslayer(TCP) and response[TCP].flags == "RA":
        print("❌ Port 80 is CLOSED (RST-ACK received)")
    else:
        print("🤔 Got something else.")

else:
    print("No response")