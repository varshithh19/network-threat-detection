from modules.firewall_controller import FirewallController
from modules.logger import SecurityLogger


class ThreatDetector:

    def __init__(self):

        # detection thresholds (lowered for demo/testing)
        self.port_scan_threshold = 5
        self.packet_rate_threshold = 10
        self.connection_threshold = 50

        self.firewall = FirewallController()
        self.logger = SecurityLogger()

        # your own machine IP (do not block this)
        self.local_ip = "192.168.1.12"

    def analyze(self, ip, stats, packet_rate):

        alerts = []

        # Detect port scanning
        if len(stats["ports"]) > self.port_scan_threshold:
            alerts.append("PORT_SCAN")

        # Detect high packet rate
        if packet_rate > self.packet_rate_threshold:
            alerts.append("TRAFFIC_FLOOD")

        # Detect too many connections
        if stats["connections"] > self.connection_threshold:
            alerts.append("CONNECTION_FLOOD")

        # Take action if alerts exist
        for alert in alerts:

            # Do NOT block your own machine
            if ip != self.local_ip:
                self.firewall.block_ip(ip)

            # Always log the threat
            self.logger.log_event(ip, alert)

        return alerts