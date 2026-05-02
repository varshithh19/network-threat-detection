import json
import os
from datetime import datetime


class SecurityLogger:

    def __init__(self):

        self.log_file = "security_logs.json"

        # create file if it doesn't exist
        if not os.path.exists(self.log_file):
            with open(self.log_file, "w") as f:
                json.dump([], f)

    def log_event(self, ip, threat):

        event = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "attacker_ip": ip,
            "threat_type": threat,
            "action": "BLOCKED"
        }

        with open(self.log_file, "r+") as f:

            data = json.load(f)
            data.append(event)

            f.seek(0)
            json.dump(data, f, indent=4)

        print(f"[LOG] Threat recorded for {ip}")