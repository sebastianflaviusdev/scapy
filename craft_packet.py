from scapy.all import *
from scapy.layers.inet import IP, ICMP

# Custom packet with ICMP
packet = IP(dst="8.8.8.8") / ICMP()

# Show packet details
packet.show()
