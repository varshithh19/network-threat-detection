from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP
import time


def process_packet(packet):

    if packet.haslayer(IP):

        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto
        timestamp = time.time()

        port = None

        if packet.haslayer(TCP):
            port = packet[TCP].dport
        elif packet.haslayer(UDP):
            port = packet[UDP].dport

        packet_info = {
            "src_ip": src_ip,
            "dst_ip": dst_ip,
            "protocol": protocol,
            "port": port,
            "timestamp": timestamp
        }

        return packet_info


def start_sniffing(callback):

    sniff(
        prn=lambda pkt: callback(process_packet(pkt)),
        store=False
    )