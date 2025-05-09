from pyvis.network import Network
import networkx as nx

# Load your GraphML file (replace this with your file path)
G = nx.read_graphml("../graph_only_hills.graphml")

# Create a PyVis network object
net = Network(height="800px", width="100%", bgcolor="#222222", font_color="white")

# Feed the NetworkX graph into PyVis
net.from_nx(G)

# Optional: Customize the visualization
net.force_atlas_2based()  # Apply a force-directed layout

# Set options for a smoother look
net.set_options("""
var options = {
  "nodes": {
    "shape": "dot",
    "size": 10,
    "color": {
      "background": "skyblue",
      "border": "white"
    },
    "font": {
      "size": 14,
      "color": "white"
    }
  },
  "edges": {
    "color": "#888",
    "width": 1,
    "smooth": {
      "type": "continuous",
      "roundness": 0.5
    }
  },
  "physics": {
    "enabled": true,
    "solver": "forceAtlas2Based",
    "stabilization": true
  }
}
""")

print(net)
# Save the interactive visualization as an HTML file
net.show("museum_network.html")
