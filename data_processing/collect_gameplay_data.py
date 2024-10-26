import json

def collect_data(agent_id, activity):
    data = {
        "agent_id": agent_id,
        "activity": activity,
        "timestamp": "2023-10-26"  # Placeholder for date
    }
    with open(f"data/{agent_id}_activity.json", "w") as file:
        json.dump(data, file)
    print(f"Data collected for agent {agent_id}")
