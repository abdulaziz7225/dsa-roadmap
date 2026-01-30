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
        print("DFS Traversal: ", end="")
        self.dfs_recursive(starting_vertex, visited)

    def dfs_recursive(self, current_vertex, visited):
        visited[current_vertex] = True
        print(current_vertex, end=" ")

        # Recur for all unvisited neighbors
        for neighbor in self.adjacency_list[current_vertex]:
            if not visited[neighbor]:
                self.dfs_recursive(neighbor, visited)


class Solution:
    @staticmethod
    def main():
        g = Graph(5)

        g.add_edge(0, 3)
        g.add_edge(0, 2)
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        g.add_edge(2, 4)

        print("DFS Traversal starting from vertex 0: ", end="")
        g.dfs(0)


if __name__ == "__main__":
    Solution.main()


# V = number of vertices, E = number of edges
# Time complexity: O(V + E)
# __init__(): O(V)
# dfs(): O(E)
# Space complexity: O(V)
# __init__(): O(V)
# dfs(): O(V)

