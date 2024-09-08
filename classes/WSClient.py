import json
import websockets
import asyncio

class WSClient:
    def __init__(self) -> None:
        self.on_message = None
        self.tasks = []

    def set_on_message(self, on_message):
        self.on_message = on_message

    def run(self, url: str):
        task = asyncio.create_task()
