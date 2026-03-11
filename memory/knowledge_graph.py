import json
import os


class KnowledgeGraph:

    def __init__(self):

        self.file = "knowledge_graph.json"

        # create graph file if it does not exist
        if not os.path.exists(self.file):
            with open(self.file, "w") as f:
                json.dump({}, f)

        with open(self.file, "r") as f:
            self.graph = json.load(f)

    def add_relation(self, topic, concept):

        topic = topic.lower()
        concept = concept.lower()

        if topic not in self.graph:
            self.graph[topic] = []

        if concept not in self.graph[topic]:
            self.graph[topic].append(concept)

        self.save()

    def get_relations(self, topic):

        topic = topic.lower()

        return self.graph.get(topic, [])

    def save(self):

        with open(self.file, "w") as f:
            json.dump(self.graph, f, indent=2)