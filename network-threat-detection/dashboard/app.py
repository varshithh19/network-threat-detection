import json
from flask import Flask, render_template

app = Flask(__name__)

LOG_FILE = "security_logs.json"


def load_logs():

    try:
        with open(LOG_FILE, "r") as f:
            return json.load(f)
    except:
        return []


@app.route("/")
def dashboard():

    logs = load_logs()

    total_attacks = len(logs)

    attackers = list(set(log["attacker_ip"] for log in logs))

    return render_template(
        "index.html",
        logs=logs,
        total_attacks=total_attacks,
        attackers=attackers
    )


if __name__ == "__main__":

    app.run(debug=True)