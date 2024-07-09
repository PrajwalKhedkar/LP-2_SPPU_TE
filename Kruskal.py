class Graph:
    def __init__(self):
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find_parent(self, parent, i):
        if parent[i] == i:
            return i
        return self.find_parent(parent, parent[i])

    def union(self, parent, rank, x, y):
        x_root = self.find_parent(parent, x)
        y_root = self.find_parent(parent, y)

        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    def kruskal_mst(self):
        result = []
        i, e = 0, 0

        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            u, v, w = self.graph[i]
            i += 1
            x = self.find_parent(parent, u)
            y = self.find_parent(parent, v)

            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        minimum_cost = 0
        print("Edges in the Minimum Spanning Tree:")
        for u, v, weight in result:
            minimum_cost += weight
            print(f"{u} - {v} : {weight}")

        print(f"\nMinimum Cost of MST: {minimum_cost}")

# Get user input for the graph
g = Graph()
n = int(input("Enter the number of vertices: "))
m = int(input("Enter the number of edges: "))
for _ in range(m):
    u, v, w = map(int, input("Enter edge (u v w): ").split())
    g.add_edge(u, v, w)

g.kruskal_mst()