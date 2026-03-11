from fastapi import FastAPI
from engine.orchestrator import Orchestrator

app = FastAPI()

engine = Orchestrator()


@app.get("/")
def root():
    return {"system": "AI University Engine"}


@app.post("/query")
def query(q: str):

    answer = engine.process(q)

    return {
        "question": q,
        "answer": answer
    }