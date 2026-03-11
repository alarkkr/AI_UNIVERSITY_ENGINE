from agents.planner_agent import PlannerAgent
from agents.retriever_agent import RetrieverAgent
from agents.reasoner_agent import ReasonerAgent
from agents.verifier_agent import VerifierAgent


class Orchestrator:

    def __init__(self):

        self.planner = PlannerAgent()
        self.retriever = RetrieverAgent()
        self.reasoner = ReasonerAgent()
        self.verifier = VerifierAgent()

    def process(self, question):

        plan = self.planner.plan(question)

        knowledge = self.retriever.retrieve(plan["query"])

        reasoning = self.reasoner.reason(knowledge)

        final = self.verifier.verify(reasoning)

        return final