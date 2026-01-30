#include <iostream>
#include <stack>
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

    void dfs(int startingVertex) {
        vector<bool> visited(vertices, false);
        stack<int> myStack;
        myStack.push(startingVertex);

        while (!myStack.empty()) {
            int curr = myStack.top();
            myStack.pop();

            if (!visited[curr]) {
                cout << curr << " ";
                visited[curr] = true;
            }

            for (auto neighbor : adjacencyList[curr]) {
                if (!visited[neighbor]) {
                    myStack.push(neighbor);
                }
            }
        }
    }
};

// V = number of vertices, E = number of edges
// Time complexity: O(V + E)
// constructor(): O(V)
// dfs(): O(E)
// Space complexity: O(V)
// constructor(): O(V)
// dfs(): O(V)