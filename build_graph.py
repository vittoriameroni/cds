import re
import spacy
import json
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict
from itertools import combinations

nlp = spacy.load('en_core_web_sm')

with open("NER_dictionnary_only_hill_names.json", "r") as file:
    NER_dictionnary = json.load(file)

with open("data/hill_list.json", "r") as file:
    hill_list = json.load(file)

# Invert data: term -> list of keys where it appears
term_to_keys = defaultdict(set)
for key, terms in NER_dictionnary.items():
    for term in terms:
        term_to_keys[term.lower()].add(key)

# Count co-occurrences between key pairs
co_occurrence = defaultdict(int)
for keys in term_to_keys.values():
    for a, b in combinations(sorted(keys), 2):
        co_occurrence[(a, b)] += 1

# Create graph
G = nx.Graph()
G.add_nodes_from(NER_dictionnary.keys())
for (a, b), weight in co_occurrence.items():
    G.add_edge(a, b, weight=weight)

for node in G.nodes:
    if node in hill_list.keys():
        G.nodes[node]['continent'] = hill_list[node]["continent"]

nx.write_graphml(G, "graph_only_hills_names.graphml")



