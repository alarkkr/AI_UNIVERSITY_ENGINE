import json
import os


class DatasetGenerator:

    def __init__(self):

        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.output_dir = os.path.join(base_dir, "trainingdir")

        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def generate_dataset(self, topic, text):

        topic = topic.lower()

        words = text.split()

        facts = []

        for i in range(0, len(words), 5):

            fact = " ".join(words[i:i+5]).strip()

            if len(fact) > 10:
                facts.append(fact)

        dataset = {
            "topic": topic,
            "facts": facts
        }

        file_path = os.path.join(self.output_dir, f"{topic}_dataset.json")

        with open(file_path, "w") as f:
            json.dump(dataset, f, indent=2)

        return file_path