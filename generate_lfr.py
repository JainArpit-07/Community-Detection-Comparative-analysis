import networkx as nx
import random

G = nx.generators.community.LFR_benchmark_graph(
    n=500,
    tau1=3,
    tau2=1.5,
    mu=0.1,
    average_degree=8,
    min_community=20
)

nx.write_edgelist(G, "lfr.edgelist")
