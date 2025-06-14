from scapy.all import *
from scapy.layers.inet import IP, ICMP, TCP

# custom packet / ICMP
packet = IP(dst="8.8.8.8") / ICMP() / Raw()

# show packet details
packet.show()
