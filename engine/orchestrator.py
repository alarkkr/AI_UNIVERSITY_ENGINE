from agents.planner_agent import PlannerAgent
from agents.retriever_agent import RetrieverAgent
from agents.reasoner_agent import ReasonerAgent
from agents.verifier_agent import VerifierAgent
from memory.vector_memory import VectorMemory


class Orchestrator:

    def __init__(self):

        self.planner = PlannerAgent()
        self.retriever = RetrieverAgent()
        self.reasoner = ReasonerAgent()
        self.verifier = VerifierAgent()

        self.memory = VectorMemory()

    def process(self, question):

        # check memory first
        stored = self.memory.search(question)

        if stored:
            return stored

        plan = self.planner.plan(question)

        knowledge = self.retriever.retrieve(plan["query"])

        reasoning = self.reasoner.reason(knowledge)

        final = self.verifier.verify(reasoning)

        # store answer
        self.memory.add(question, final)

        return final