from ai_agents.resource_gatherer import ResourceGatherer
from ai_agents.builder import Builder
from ai_agents.explorer import Explorer

def main():
    gatherer = ResourceGatherer(agent_id="RG01", resource_type="wood")
    builder = Builder(agent_id="B01")
    explorer = Explorer(agent_id="E01")

    gatherer.gather_resources()
    builder.build_structure("house")
    explorer.explore_area("cave")

if __name__ == "__main__":
    main()
