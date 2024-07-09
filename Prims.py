import heapq

def prims_algorithm(graph):
    mst = []
    visited = set()
    start_vertex = next(iter(graph))
    visited.add(start_vertex)
    edges = [(cost, start_vertex, v) for v, cost in graph[start_vertex]]
    heapq.heapify(edges)
    
    while edges:
        cost, u, v = heapq.heappop(edges)
        if v not in visited:
            visited.add(v)
            mst.append((u, v, cost))
            for next_vertex, next_cost in graph[v]:
                if next_vertex not in visited:
                    heapq.heappush(edges, (next_cost, v, next_vertex))
    
    return mst

def get_graph_input():
    graph = {}
    num_edges = int(input("Enter the number of edges: "))
    for _ in range(num_edges):
        u, v, cost = input("Enter edge (source destination cost): ").split()
        cost = int(cost)
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append((v, cost))
        graph[v].append((u, cost))  # Assuming undirected graph
    return graph

def main():
    graph = get_graph_input()
    mst = prims_algorithm(graph)
    print("Minimum Spanning Tree (Prim's Algorithm):")
    for edge in mst:
        print(edge)

if __name__ == "__main__":
    main()
