from agents.planner_agent import PlannerAgent
from agents.retriever_agent import RetrieverAgent
from agents.reasoner_agent import ReasonerAgent
from agents.verifier_agent import VerifierAgent

from memory.vector_memory import VectorMemory
from memory.knowledge_graph import KnowledgeGraph


class Orchestrator:

    def __init__(self):

        self.planner = PlannerAgent()
        self.retriever = RetrieverAgent()
        self.reasoner = ReasonerAgent()
        self.verifier = VerifierAgent()

        self.memory = VectorMemory()
        self.graph = KnowledgeGraph()

    def process(self, question):

        # check vector memory first
        stored = self.memory.search(question)

        if stored:
            return stored

        # agent pipeline
        plan = self.planner.plan(question)

        knowledge = self.retriever.retrieve(plan["query"])

        reasoning = self.reasoner.reason(knowledge)

        final = self.verifier.verify(reasoning)

        # store answer in vector memory
        self.memory.add(question, final)

        # extract relations for knowledge graph
        words = final.split()

        for w in words:

            w = w.strip(",.()[]{}")

            if len(w) > 5:
                self.graph.add_relation(question, w)

        return final