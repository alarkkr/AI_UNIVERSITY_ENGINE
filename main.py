from engine.orchestrator import Orchestrator

engine = Orchestrator()

print("AI University Engine CLI (type 'exit' to quit)\n")

while True:
    q = input(">> ")

    if q.lower() == "exit":
        break

    response = engine.process(q)
    print("\n", response, "\n")