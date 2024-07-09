import heapq

def dijkstra(graph, start, destination):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    previous_vertices = {vertex: None for vertex in graph}
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        if current_vertex == destination:
            path = []
            while previous_vertices[current_vertex] is not None:
                path.insert(0, current_vertex)
                current_vertex = previous_vertices[current_vertex]
            path.insert(0, start)
            return path, distances[destination]
        
        if current_distance > distances[current_vertex]:
            continue
        
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_vertices[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return [], float('inf')

def get_graph_input():
    graph = {}
    num_vertices = int(input("Enter the number of vertices: "))
    num_edges = int(input("Enter the number of edges: "))
    
    for _ in range(num_edges):
        u, v, weight = input("Enter edge (source destination weight): ").split()
        weight = int(weight)
        
        if u not in graph:
            graph[u] = {}
        if v not in graph:
            graph[v] = {}
        
        graph[u][v] = weight
        graph[v][u] = weight  # Assuming undirected graph
    
    return graph

def main():
    graph = get_graph_input()
    start_vertex = input("Enter the starting vertex: ")
    destination_vertex = input("Enter the destination vertex: ")
    
    path, shortest_distance = dijkstra(graph, start_vertex, destination_vertex)
    
    if path:
        print(f"The shortest path from {start_vertex} to {destination_vertex} is:")
        print(" -> ".join(path), f"(distance: {shortest_distance})")
    else:
        print(f"There is no path from {start_vertex} to {destination_vertex}.")

if __name__ == "__main__":
    main()
