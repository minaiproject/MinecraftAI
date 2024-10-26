import torch
from torch.utils.data import DataLoader
from agent_model import AgentModel

def train(model, data_loader, epochs=5, learning_rate=0.001):
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
    loss_fn = torch.nn.CrossEntropyLoss()

    for epoch in range(epochs):
        for inputs, labels in data_loader:
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = loss_fn(outputs, labels)
            loss.backward()
            optimizer.step()
        print(f"Epoch {epoch + 1}/{epochs}, Loss: {loss.item()}")

# Assuming data_loader is predefined
# model = AgentModel(input_size=10, hidden_size=20, output_size=3)
# train(model, data_loader)
