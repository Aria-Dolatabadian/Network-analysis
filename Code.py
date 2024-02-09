
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Step 1: Read Data from CSV
df = pd.read_csv('microorganism_interaction_data.csv')

# Step 2: Network Analysis
G = nx.from_pandas_edgelist(df, 'Microorganism', 'Element', create_using=nx.Graph())
pos = nx.spring_layout(G)  # Positions for all nodes

# Get unique microorganisms and elements
microorganisms = df['Microorganism'].unique()
elements = df['Element'].unique()

# Assign unique colors to each microorganism and element
num_microorganisms = len(microorganisms)
num_elements = len(elements)
microorganism_colors = plt.cm.tab20(np.linspace(0, 1, num_microorganisms))
element_colors = plt.cm.tab20b(np.linspace(0, 1, num_elements))

# Create a dictionary to map elements to their corresponding colors
element_color_dict = dict(zip(elements, element_colors))

# Step 3: Plot Network Interaction with Unique Colors
plt.figure(figsize=(10, 8))

# Draw nodes with unique colors for microorganisms
for i, microorganism in enumerate(microorganisms):
    nx.draw_networkx_nodes(G, pos, nodelist=[microorganism], node_color=microorganism_colors[i], node_size=3000)

# Draw nodes with unique colors for elements, with smaller size
for i, element in enumerate(elements):
    nx.draw_networkx_nodes(G, pos, nodelist=[element], node_color=element_colors[i], node_size=1000)

# Draw edges with corresponding element colors
edge_colors = []
for edge in G.edges():
    if edge[1] in element_color_dict:
        edge_colors.append(element_color_dict[edge[1]])
    else:
        edge_colors.append('gray')  # Default color for edges not connecting elements
nx.draw_networkx_edges(G, pos, edge_color=edge_colors)

# Draw labels
nx.draw_networkx_labels(G, pos, font_size=10, font_color='black')

plt.title('Network Interaction between Microorganisms and Elements')
plt.axis('off')
plt.show()
