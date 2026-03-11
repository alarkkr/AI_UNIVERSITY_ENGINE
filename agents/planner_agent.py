class PlannerAgent:

    def plan(self, question):

        return {
            "query": question,
            "strategy": "retrieve_then_reason"
        }