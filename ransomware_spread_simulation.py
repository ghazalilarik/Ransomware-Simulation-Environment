import networkx as nx
import random
import matplotlib.pyplot as plt
import logging
import time

# Set up logging
logging.basicConfig(filename='ransomware_simulation.log', level=logging.INFO, format='%(asctime)s %(message)s')

# Number of nodes in the simulated peer-to-peer network
NUM_NODES = 20
# Probability that a node will be initially infected
INITIAL_INFECTED_PROB = 0.1
# Probability of infection spread to neighboring nodes
INFECTION_SPREAD_PROB = 0.3
# List of available mitigation strategies
MITIGATION_STRATEGIES = ["isolation", "patch", "backup"]

# Create a peer-to-peer network graph
def create_network(num_nodes):
    G = nx.erdos_renyi_graph(num_nodes, 0.2)
    # Assign each node a status
    for node in G.nodes():
        G.nodes[node]['status'] = 'healthy' if random.random() > INITIAL_INFECTED_PROB else 'infected'
    return G

# Visualize the network graph
def visualize_network(G, title="Network Status"):
    colors = ['green' if G.nodes[node]['status'] == 'healthy' else 'red' for node in G.nodes()]
    pos = nx.spring_layout(G)
    plt.figure(figsize=(10, 7))
    nx.draw(G, pos, with_labels=True, node_color=colors, node_size=500, font_size=10, font_color='white')
    plt.title(title)
    plt.show()

# Simulate ransomware spread over the network
def spread_infection(G):
    new_infections = []
    for node in G.nodes():
        if G.nodes[node]['status'] == 'infected':
            for neighbor in G.neighbors(node):
                if G.nodes[neighbor]['status'] == 'healthy' and random.random() < INFECTION_SPREAD_PROB:
                    new_infections.append(neighbor)
                    logging.info(f"Node {neighbor} got infected by node {node}")
    for node in new_infections:
        G.nodes[node]['status'] = 'infected'
    return len(new_infections) > 0

# Apply mitigation strategy to the network
def apply_mitigation(G, strategy):
    logging.info(f"Applying mitigation strategy: {strategy}")
    if strategy == "isolation":
        for node in list(G.nodes()):
            if G.nodes[node]['status'] == 'infected':
                neighbors = list(G.neighbors(node))
                G.remove_edges_from((node, neighbor) for neighbor in neighbors)
                logging.info(f"Node {node} isolated from network.")
    elif strategy == "patch":
        for node in G.nodes():
            if G.nodes[node]['status'] == 'healthy' and random.random() < 0.5:
                G.nodes[node]['status'] = 'patched'
                logging.info(f"Node {node} patched and is immune to infection.")
    elif strategy == "backup":
        for node in G.nodes():
            if G.nodes[node]['status'] == 'infected' and random.random() < 0.5:
                G.nodes[node]['status'] = 'healthy'
                logging.info(f"Node {node} restored from backup.")

# Main simulation loop
def run_simulation():
    G = create_network(NUM_NODES)
    visualize_network(G, title="Initial Network Status")
    logging.info("Starting ransomware spread simulation")

    round_counter = 0
    while True:
        round_counter += 1
        logging.info(f"Simulation round {round_counter}")
        new_infections = spread_infection(G)
        visualize_network(G, title=f"Network Status After Round {round_counter}")
        time.sleep(1)  # Pause to visualize each round

        if not new_infections:
            logging.info("No new infections detected. The spread has stopped.")
            break

        # Apply random mitigation strategy every 3 rounds
        if round_counter % 3 == 0:
            strategy = random.choice(MITIGATION_STRATEGIES)
            apply_mitigation(G, strategy)
            visualize_network(G, title=f"Network Status After Mitigation: {strategy.title()}")

    logging.info("Simulation complete")
    visualize_network(G, title="Final Network Status")

if __name__ == "__main__":
    run_simulation()
