import argparse
from pythonosc import udp_client

class OSCClient:
    def __init__(self,) -> None:
        self.is_running = False
        self.client = None

    def run(self, ip: str, port: int):
        print("ip: " + ip)
        print("port: " + str(port))
        parser = argparse.ArgumentParser()
        parser.add_argument("--ip", type=str, default=ip,
            help="The ip of the OSC server")
        parser.add_argument("--port", type=int, default=port,
            help="The port the OSC server is listening on")
        args = parser.parse_args()

        self.client = udp_client.SimpleUDPClient(args.ip, args.port)

        print("start osc")

        self.is_running = True

    def send(self, endpoint: str, value) -> None:
        if not self.is_running:
            return
        else:
            self.client.send_message(endpoint, value)

