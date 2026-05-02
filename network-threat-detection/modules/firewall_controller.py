import subprocess


class FirewallController:

    def __init__(self):
        self.blocked_ips = set()

    def block_ip(self, ip):

        if ip in self.blocked_ips:
            return

        rule_name = f"Block_{ip}"

        command = [
            "netsh",
            "advfirewall",
            "firewall",
            "add",
            "rule",
            f"name={rule_name}",
            "dir=in",
            "action=block",
            f"remoteip={ip}"
        ]

        try:
            subprocess.run(command, capture_output=True)
            self.blocked_ips.add(ip)
            print(f"[FIREWALL] Blocked IP: {ip}")

        except Exception as e:
            print(f"[FIREWALL ERROR] {e}")