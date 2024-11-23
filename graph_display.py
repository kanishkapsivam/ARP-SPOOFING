import matplotlib.pyplot as plt
import networkx as nx

# Create a graph to represent the network
def create_graph():
    G = nx.Graph()
    G.add_node("User A", color='green')
    G.add_node("User B", color='green')
    G.add_node("Attacker", color='red')

    G.add_edge("User A", "User B", color='blue', label="Normal Communication")
    G.add_edge("User A", "Attacker", color='red', label="ARP Attack")
    G.add_edge("User B", "Attacker", color='red', label="ARP Attack")
    
    return G

# Update the graph when an attack is detected or communication is normal
def update_graph(G, attack_detected=False):
    plt.clf()  # Clear the figure to update the plot

    # Set node colors based on attack detection
    node_colors = [data['color'] for _, data in G.nodes(data=True)]
    edge_colors = [data['color'] for _, _, data in G.edges(data=True)]

    # Create plot with updated data
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color=node_colors, edge_color=edge_colors, node_size=3000, font_size=12, font_weight='bold')
    
    # Display different labels based on attack detection
    if attack_detected:
        nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): G[u][v]['label'] for u, v in G.edges()}, font_size=8)
    
    # Display the graph
    plt.title("ARP Spoofing Detection Network")
    plt.pause(1)  # Pause to make the plot update dynamically

# Run the graph creation and update
def run_graph():
    G = create_graph()
    plt.ion()  # Turn on interactive mode for real-time updates
    plt.figure(figsize=(8, 6))
    plt.title("ARP Spoofing Detection Network")
    
    while True:
        update_graph(G, attack_detected=False)  # Initially, no attack
        plt.pause(3)  # Wait 3 seconds before re-updating (or you can adjust as needed)

if __name__ == "__main__":
    run_graph()
