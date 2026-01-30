from collections import deque


class Graph:
    def __init__(self, vertices: int):
        self.vertices = vertices
        self.adjacency_list = [[] for _ in range(vertices)]

    def add_edge(self, source: int, destination: int):
        self.adjacency_list[source].append(destination)
        self.adjacency_list[destination].append(source)

    def bfs(self, starting_vertex: int):
        visited = [False] * self.vertices
        queue = deque()

        visited[starting_vertex] = True
        queue.append(starting_vertex)

        while queue:
            curr = queue.popleft()
            print(curr, end=" ")

            for neighbor in self.adjacency_list[curr]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

# V = number of vertices, E = number of edges
# Time complexity: O(V + E)
# __init__(): O(V)
# bfs(): O(V + E)
# Space complexity: O(V)
# __init__(): O(V)
# bfs(): O(V)
