import time
from collections import defaultdict
from modules.threat_detector import ThreatDetector


class TrafficAnalyzer:

    def __init__(self):

        self.ip_stats = defaultdict(lambda: {
            "connections": 0,
            "ports": set(),
            "packet_count": 0,
            "timestamps": []
        })

        self.detector = ThreatDetector()


    def process_packet(self, packet):

        if packet is None:
            return

        src_ip = packet["src_ip"]
        port = packet["port"]
        timestamp = packet["timestamp"]

        stats = self.ip_stats[src_ip]

        stats["connections"] += 1
        stats["packet_count"] += 1
        stats["timestamps"].append(timestamp)

        if port:
            stats["ports"].add(port)

        self.cleanup_old_packets(src_ip)

    def cleanup_old_packets(self, ip):

        now = time.time()
        stats = self.ip_stats[ip]

        stats["timestamps"] = [
            t for t in stats["timestamps"]
            if now - t <= 10
        ]

    def get_packet_rate(self, ip):

        stats = self.ip_stats[ip]
        return len(stats["timestamps"]) / 10

    def print_statistics(self):

        print("\n--- Traffic Statistics ---")

        for ip, stats in self.ip_stats.items():

            rate = self.get_packet_rate(ip)

            print(
                f"IP: {ip} | "
                f"Connections: {stats['connections']} | "
                f"Ports: {list(stats['ports'])} | "
                f"Packets/sec: {rate:.2f}"
            )

            alerts = self.detector.analyze(ip, stats, rate)

            for alert in alerts:
                print(f"[ALERT] {alert} detected from {ip}")