from fastapi import FastAPI
from engine.orchestrator import Orchestrator
from api.security import validate_input
app = FastAPI()

engine = Orchestrator()


@app.get("/")
def root():
    return {"system": "AI University Engine"}


@app.post("/query")
def query(q: str):

    answer = engine.process(q)
	q = validate_input(q)
    return {
        "question": q,
        "answer": answer
    }
@app.get("/health")
def health():
    return {"status": "running"}