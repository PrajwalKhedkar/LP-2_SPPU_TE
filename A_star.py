import heapq
def heuristic(node, goal):
    # For simplicity, we use Manhattan distance as heuristic
    x1, y1 = node
    x2, y2 = goal
    return abs(x1 - x2) + abs(y1 - y2)

def astar(graph, start, goal):
    open_list = [(0, start)]
    heapq.heapify(open_list)
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic(start, goal)

    while open_list:
        current = heapq.heappop(open_list)[1]
        if current == goal:
            path = reconstruct_path(came_from, goal)
            return path

        for neighbor, weight in graph[current]:
            tentative_g_score = g_score[current] + weight
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_list, (f_score[neighbor], neighbor))

    return None

def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    return total_path[::-1]

def main():
    graph = {}

    while True:
        print("\n1. Add Edge")
        print("2. Find Shortest Path using A* Algorithm")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            u = tuple(map(int, input("Enter source vertex (x, y): ").split()))
            v = tuple(map(int, input("Enter destination vertex (x, y): ").split()))
            w = int(input("Enter weight for the edge: "))
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            graph[u].append((v, w))
            graph[v].append((u, w))
        elif choice == '2':
            start = tuple(map(int, input("Enter starting vertex (x, y): ").split()))
            goal = tuple(map(int, input("Enter goal vertex (x, y): ").split()))
            path = astar(graph, start, goal)
            if path:
                print("Shortest path:", path)
            else:
                print("No path found!")
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please choose a valid option.")

if __name__ == "__main__":
    main()
