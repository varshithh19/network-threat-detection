from modules.packet_sniffer import start_sniffing
from modules.traffic_analyzer import TrafficAnalyzer
import threading
import time


analyzer = TrafficAnalyzer()


def packet_handler(packet):

    analyzer.process_packet(packet)


def stats_printer():

    while True:
        time.sleep(5)
        analyzer.print_statistics()


if __name__ == "__main__":

    print("Starting Network Monitor...")

    thread = threading.Thread(target=stats_printer)
    thread.daemon = True
    thread.start()

    start_sniffing(packet_handler)