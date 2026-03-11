import json
import os


class VectorMemory:

    def __init__(self):

        self.file = "memory_store.json"

        if not os.path.exists(self.file):
            with open(self.file, "w") as f:
                json.dump({}, f)

        with open(self.file, "r") as f:
            self.data = json.load(f)

    def search(self, query):

        return self.data.get(query)

    def add(self, query, answer):

        self.data[query] = answer

        with open(self.file, "w") as f:
            json.dump(self.data, f, indent=2)