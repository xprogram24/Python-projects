import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


#TASK 1: Representing a Search Problem
#---Represent a problem as a graph or state space using an adjacency list or dictionary

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'F': 3},
    'D': {'B': 2, 'E': 1},
    'E': {'B': 5, 'D': 1, 'F': 2},
    'F': {'C': 3, 'E': 2}
}

start_node = 'A'
goal_node = 'F'

# b. Define start and goal nodes
Goals = {
    'A': 7, 'B': 6, 'C': 2, 'D': 1, 'E': 0, 'F': 3
}


#. Visualize the graph using networkx or hand-drawn diagrams
def visualize_graph(graph):
    G = nx.Graph()
    for node, neighbors in graph.items():
        for neighbor, weight in neighbors.items():
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G, seed=42) 
    edge_labels = nx.get_edge_attributes(G, 'weight')

    plt.figure(figsize=(7, 5))
    nx.draw(
        G, pos, with_labels=True, node_color='skyblue', node_size=1500,
        font_size=12, font_weight='bold', edge_color='gray'
    )
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title("Graph Representation for Search Problem", fontsize=14)
    plt.show()

visualize_graph(graph)

# TASK 2: Implement Breadth-First Search (BFS)
#bfs function
def bfs(graph, start,goal):
    visited = []
    queue = deque([[start]])  # queue holds paths

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node not in visited:
            visited.append(node)

            if node == goal:
                return path, visited  # path is found

            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None, visited

def visualize_bfs_path(graph, path):
    G = nx.Graph()
    for node, neighbors in graph.items():
        for neighbor, weight in neighbors.items():
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G, seed=42)
    edge_labels = nx.get_edge_attributes(G, 'weight')

    plt.figure(figsize=(7,5))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1500,
            font_size=12, font_weight='bold', edge_color='gray')

    # Highlight the BFS path in red
    path_edges = list(zip(path, path[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=3, edge_color='red')

    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title("BFS Path from {} to {}".format(path[0], path[-1]))
    plt.show()

#
if __name__ == "__main__":
    path, visited = bfs(graph, start_node, goal_node)

    print("Order of Node Expansion:", visited)
    print("Path from {} to {}: {}".format(start_node, goal_node, path))
    print("Number of Nodes Visited:", len(visited))
    print("Is Path Optimal? → Yes, BFS is optimal for unweighted graphs.")

    # visualize the BFS path
    visualize_bfs_path(graph, path)


#  TASK 3: Implement Depth-First Search (DFS)
def dfs(graph, start, goal, visited=None, path=None):
    if visited is None:
        visited = []
    if path is None:
        path = []

    visited.append(start)
    path.append(start)

    #when goal is reached will return path
    if  start == goal:
        return path, visited
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            new_path, visited =  dfs(graph, neighbor, goal, visited, path.copy())
            if new_path:
                return new_path, visited
            
    return None, visited


def visualize_dfs_path(graph, path):
    G = nx.Graph()
    for node, neighbors in graph.items():
        for neighbors, weight in neighbors.items():
            G.add_edge(node, neighbors, weight=weight)

    pos = nx.spring_layout(G, seed=42)
    edge_labels = nx.get_edge_attributes(G, 'weight')

    plt.figure(figsize=(7,5))
    nx.draw(G, pos, with_labels=True, node_color='lightblue',
            node_size=1500, font_size=12, font_weight='bold', edge_color='gray')

    # Highlight DFS path in purple
    path_edges = list(zip(path, path[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=3, edge_color='purple')

    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title("DFS Path from {} to {}".format(path[0], path[-1]))
    plt.show()

if __name__ == "__main__":
    path, visited = dfs(graph, start_node, goal_node)

    print("Order of Node Exploration:", visited)
    print("Path found (DFS):", path)
    print("Number of Nodes Visited:", len(visited))

    # DFS is not guaranteed to find the shortest path
    print("\nNote: DFS might NOT find the shortest path because it explores depth-first.")
    print("For example, BFS would find ['A', 'C', 'F'] as shorter, but DFS may find a longer one.")

    # Visualize DFS path
    visualize_dfs_path(graph, path)