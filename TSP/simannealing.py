import random
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from networkx.algorithms.approximation import traveling_salesman_problem


def comp_graph(n, w_range = (1, 100)):
    G = nx.complete_graph(n)

    for u, v in G.edges():
        G.edges[u, v]['weight'] = random.randint(*w_range)

    return G

def plot(G, tour, u, config):
    plt.clf()

    nx.draw(G, config, with_labels = True, node_color='lightblue', node_size=500, edgelist=[])
    e = list(zip(tour, tour[1:]))
    nx.draw_networkx_edges(G, config, edgelist=e, edge_color='red', width=2)
    nx.draw_networkx_nodes(G, config, nodelist=[u], node_color='green', node_size=500)

    # plt.pause(0.001)

def cost(G, tour):
    return sum(G[tour[i]][tour[i+1]]['weight'] for i in range(len(tour)-1))



n = 10
G = comp_graph(n)
config = nx.spring_layout(G)

cur_tour = [x for x in range(n)]
random.shuffle(cur_tour)
best_tour = cur_tour


i, j = random.randint(0, n-1), random.randint(0, n-1)
cur_tour[i], cur_tour[j] = cur_tour[j], cur_tour[i]


T = 1000
N = 10

plt.ion()
plt.show()

while (T):

    for i in range(N):
        i, j = random.randint(0, n-1), random.randint(0, n-1)

        e1 = cost(G, cur_tour + [cur_tour[0]])
        cur_tour[i], cur_tour[j] = cur_tour[j], cur_tour[i]
        e2 = cost(G, cur_tour + [cur_tour[0]])

        de = e1 - e2

        if de <= 0 and random.uniform(0, 1) > np.exp(de/T):
            cur_tour[i], cur_tour[j] = cur_tour[j], cur_tour[i]

        # plot(G, cur_tour + [cur_tour[0]], 0, config)
        
        if cost(G, best_tour) > cost(G, cur_tour):
            best_tour = cur_tour


    T-=1

plt.ioff()
plt.show()

approximate_tour = traveling_salesman_problem(G, cycle=True)
approximate_tour_cost = cost(G, approximate_tour)

print("networkx:")
print(approximate_tour)
print(approximate_tour_cost)

print("simulated annealing:")
print(best_tour)
print(cost(G, best_tour))
        