#include <iostream>
#include <vector>

using namespace std;

class Solution {
  private:
    int capacity;
    int front, back;
    vector<int> queue;

  public:
    Solution(int capacity)
        : capacity(capacity), front(-1), back(-1), queue(capacity) {};

    bool isEmpty(void) { return front == -1; }

    bool isFull(void) { return ((back + 1) % capacity == front); }

    int getSize(void) {
        if (isEmpty())
            return 0;
        else if (front <= back)
            return (back - front + 1);
        return capacity + (back - front + 1);
    }

    // 0 = success, 1 = empty
    int getFront(int &value) {
        if (isEmpty())
            return 1;
        value = queue.at(front);
        return 0;
    }

    // 0 = success, 1 = empty
    int getBack(int &value) {
        if (isEmpty())
            return 1;
        value = queue.at(back);
        return 0;
    }

    // 0 = success, 1 = full
    int enque(int element) {
        if (isFull())
            return 1;

        if (isEmpty())
            front = back = 0;
        else
            back = (back + 1) % capacity;
        queue.at(back) = element;
        return 0;
    }

    // 0 = success, 1 = empty
    int deque() {
        if (isEmpty())
            return 1;

        if (front == back)
            front = back = -1;
        else
            front = (front + 1) % capacity;
        return 0;
    }
};
