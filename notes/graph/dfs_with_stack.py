class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        # Adjacency list
        self.adjacency_list = [[] for _ in range(vertices)]

    def add_edge(self, source, destination):
        self.adjacency_list[source].append(destination)
        # For an undirected graph
        self.adjacency_list[destination].append(source)

    def dfs(self, starting_vertex):
        visited = [False] * self.vertices
        stack = []

        stack.append(starting_vertex)

        while stack:
            current_vertex = stack.pop()

            if not visited[current_vertex]:
                # Process the current node
                print(current_vertex, end=" ")
                visited[current_vertex] = True

            # Push all unvisited neighbors onto the stack
            for neighbor in self.adjacency_list[current_vertex]:
                if not visited[neighbor]:
                    stack.append(neighbor)

# V = number of vertices, E = number of edges
# Time complexity: O(V + E)
# __init__(): O(V)
# dfs(): O(E)
# Space complexity: O(V)
# __init__(): O(V)
# dfs(): O(V)
