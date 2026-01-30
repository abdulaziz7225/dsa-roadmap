#include <iostream>
#include <queue>
#include <vector>

using namespace std;

class Graph {
  private:
    int vertices;
    vector<vector<int>> adjacencyList;

  public:
    Graph(int vertices) : vertices(vertices), adjacencyList(vertices) {}

    void addEdge(int source, int destination) {
        adjacencyList[source].push_back(destination);
        adjacencyList[destination].push_back(source);
    }

    void bfs(int startingVertex) {
        vector<bool> visited(vertices, false);
        queue<int> myQueue;

        visited[startingVertex] = true;
        myQueue.push(startingVertex);

        while (!myQueue.empty()) {
            int curr = myQueue.front();
            myQueue.pop();

            visited[curr] = true;
            cout << curr << " ";

            for (auto neighbor : adjacencyList[curr]) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    myQueue.push(neighbor);
                }
            }
        }
    }
};

// V = number of vertices, E = number of edges
// Time complexity: O(V + E)
// constructor(): O(V)
// bfs(): O(V + E)
// Space complexity: O(V)
// constructor(): O(V)
// bfs(): O(V)
