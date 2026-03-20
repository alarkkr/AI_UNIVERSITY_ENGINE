from agents.planner_agent import PlannerAgent
from agents.retriever_agent import RetrieverAgent
from agents.reasoner_agent import ReasonerAgent
from agents.verifier_agent import VerifierAgent

from memory.vector_memory import VectorMemory
from memory.knowledge_graph import KnowledgeGraph
from engine.dataset_generator import DatasetGenerator


class Orchestrator:

    def __init__(self):

        self.planner = PlannerAgent()
        self.retriever = RetrieverAgent()
        self.reasoner = ReasonerAgent()
        self.verifier = VerifierAgent()

        self.memory = VectorMemory()
        self.graph = KnowledgeGraph()
        self.dataset = DatasetGenerator()

    def process(self, question):

        # Check vector memory cache
        stored = self.memory.search(question)

        if stored:
            return stored

        # Planning stage
        plan = self.planner.plan(question)

        # Retrieval stage
        knowledge = self.retriever.retrieve(plan["query"])

        # Reasoning stage (LLM)
        reasoning = self.reasoner.reason(knowledge)

        # Verification stage
        final = self.verifier.verify(reasoning)

        # Store memory
        self.memory.add(question, final)

        # Generate dataset entry
        self.dataset.generate_dataset(question, final)

        return final