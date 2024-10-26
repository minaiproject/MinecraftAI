class ResourceGatherer:
    def __init__(self, agent_id, resource_type):
        self.agent_id = agent_id
        self.resource_type = resource_type

    def gather_resources(self):
        print(f"Agent {self.agent_id} is gathering {self.resource_type}.")
        # Add resource-gathering logic here
