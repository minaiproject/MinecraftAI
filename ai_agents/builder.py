class Builder:
    def __init__(self, agent_id):
        self.agent_id = agent_id

    def build_structure(self, structure_type):
        print(f"Agent {self.agent_id} is building a {structure_type}.")
        # Add building logic here
