#include <iostream>
#include <vector>

using namespace std;

class Graph {
  private:
    int vertices;
    vector<vector<int>> adjacencyList;

    void dfsRecursive(int curr, vector<bool> &visited) {
        visited[curr] = true;
        cout << curr << " ";

        for (auto neighbor : adjacencyList[curr]) {
            if (!visited[neighbor]) {
                dfsRecursive(neighbor, visited);
            }
        }
    }

  public:
    Graph(int vertices) : vertices(vertices), adjacencyList(vertices) {}

    void addEdge(int source, int destination) {
        adjacencyList[source].push_back(destination);
        adjacencyList[destination].push_back(source);
    }

    void dfs(int startingVertex) {
        vector<bool> visited(vertices, false);
        cout << "DFS Traversal: ";
        dfsRecursive(startingVertex, visited);
    }
};

// V = number of vertices, E = number of edges
// Time complexity: O(V + E)
// constructor(): O(V)
// dfs(): O(E)
// Space complexity: O(V)
// constructor(): O(V)
// dfs(): O(V)