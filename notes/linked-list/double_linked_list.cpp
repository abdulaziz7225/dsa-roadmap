struct ListNode {
    int val;
    ListNode *prev;
    ListNode *next;
    ListNode() : val(0), prev(nullptr), next(nullptr) {}
    ListNode(int x) : val(x), prev(nullptr), next(nullptr) {}
    ListNode(int x, ListNode *prev, ListNode *next)
        : val(x), prev(prev), next(next) {}
};