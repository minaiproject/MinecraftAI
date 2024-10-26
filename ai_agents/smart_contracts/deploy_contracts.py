from solana.rpc.api import Client
from solana_utils import deploy_contract

def main():
    client = Client("https://api.mainnet-beta.solana.com")
    contract_address = deploy_contract(client, "contracts/AgentManagement.sol")
    print(f"Contract deployed at: {contract_address}")

if __name__ == "__main__":
    main()
