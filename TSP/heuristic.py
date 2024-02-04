import random
import networkx as nx
import matplotlib.pyplot as plt 

from networkx.algorithms.approximation import traveling_salesman_problem

### SOURCE : https://www.youtube.com/watch?v=r9lzHs2rZDc
### Used as comparison to simulated annealing

def completegraph(num_nodes, weight_range=(1, 100)):
    G = nx.complete_graph(num_nodes)

    for u, v in G.edges():
        G.edges[u, v]['weight'] = random.randint(*weight_range)

    return G 


def plot_graph_step(G, tour, current_node, pos):
    print(tour)
    plt.clf()
    # remove edgelist paramter to show all edges
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, edgelist=[])
    path_edges = list(zip(tour, tour[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)
    nx.draw_networkx_nodes(G, pos, nodelist=[current_node], node_color='green', node_size=500)

    # labels on edges

    # only labels on tour
    # edge_labels = dict(zip(path_edges, [G[u][v]['weight'] for u, v in path_edges]))
    # all labels
    # edge_labels = nx.get_edge_attributes(G, 'weight')  

    # nx.draw_networkx_edge_labels(0, pos, edge_labels=edge_labels)

    plt.pause(0.5)

def calculate_tour_cost(G, tour):
    return sum(G[tour[i]][tour[i+1]]['weight'] for i in range(len(tour)-1))


def nearest_neighbour_tsp(G, start_node=None):
    if start_node is None:
        start_node = random.choice(list(G.nodes))

    pos = nx.spring_layout(G)
    plt.ion()
    plt.show()

    unvisited = set(G.nodes)
    unvisited.remove(start_node)
    tour = [start_node]
    current_node = start_node

    plot_graph_step(G, tour, current_node, pos)

    while unvisited:
        next_node = min(unvisited, key=lambda node: G[current_node][node]['weight'])
        unvisited.remove(next_node)
        tour.append(next_node)
        current_node = next_node
        plot_graph_step(G, tour, current_node, pos)


    tour.append(start_node)
    
    plot_graph_step(G, tour, current_node, pos)

    print(tour)
    tour_cost = calculate_tour_cost(G, tour)
    print(f"Construction heuristic tour cost: {tour_cost}")

    plt.ioff()
    plt.show()



G = completegraph(10)

approximate_tour = traveling_salesman_problem(G, cycle=True)
approximate_tour_cost = calculate_tour_cost(G, approximate_tour)

print(approximate_tour)
print(approximate_tour_cost)

nearest_neighbour_tsp(G, 0)