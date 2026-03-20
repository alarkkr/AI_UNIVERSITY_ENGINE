import requests


class ReasonerAgent:

    def __init__(self):
        self.url = "http://127.0.0.1:11434/api/generate"
        self.model = "mistral"

    def reason(self, knowledge):

        prompt = f"""
Explain the following concept clearly in English.

Concept: {knowledge}

Write a short paragraph explanation.
"""

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }

        try:

            r = requests.post(self.url, json=payload, timeout=120)

            if r.status_code == 200:
                data = r.json()

                if "response" in data and len(data["response"].strip()) > 10:
                    return data["response"].strip()

        except Exception as e:
            print("LLM ERROR:", e)

        return f"No explanation generated for {knowledge}"