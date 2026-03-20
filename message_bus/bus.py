import json

class MessageBus:

    def send(self, message):
        return json.dumps(message)

    def receive(self, message_str):
        return json.loads(message_str)