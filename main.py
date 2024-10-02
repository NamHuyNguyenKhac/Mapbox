import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt

place_name = "Hanoi, Vietnam"

# Tải dữ liệu đường phố từ OpenStreetMap
G = ox.graph_from_place(place_name, network_type='drive')

# Plot the street network
fig, ax = ox.plot_graph(G, bgcolor='k', node_size=5, edge_color='#ffffff', edge_linewidth=0.5)
plt.show()

fig, ax = ox.plot_graph(G, save=True, filepath="hanoi_map_drive.png", bgcolor='k', node_size=5, edge_color='#ffffff', edge_linewidth=0.5)
