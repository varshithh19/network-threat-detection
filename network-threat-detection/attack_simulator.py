import socket
import time
import random


TARGET_IP = "192.168.1.12"
PORT_RANGE = range(1, 1000)
DELAY = 0.01


def port_scan():

    print("[SIMULATOR] Starting port scan attack...\n")

    for port in PORT_RANGE:

        try:

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.05)

            s.connect((TARGET_IP, port))

            print(f"[SCAN] Port {port} open")

            s.close()

        except:
            pass

        time.sleep(DELAY)

    print("\n[SIMULATOR] Scan finished")


def connection_flood():

    print("[SIMULATOR] Starting connection flood...\n")

    for i in range(500):

        try:

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            port = random.randint(20, 200)

            s.settimeout(0.05)
            s.connect((TARGET_IP, port))

            s.close()

        except:
            pass

    print("\n[SIMULATOR] Flood finished")


if __name__ == "__main__":

    print("\n1. Port Scan Attack")
    print("2. Connection Flood\n")

    choice = input("Choose attack type: ")

    if choice == "1":
        port_scan()

    elif choice == "2":
        connection_flood()

    else:
        print("Invalid option")