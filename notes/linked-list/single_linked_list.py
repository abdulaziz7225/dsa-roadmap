from typing import Optional


class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next: Optional["ListNode"] = None


class Solution:
    def __init__(self):
        self.head: Optional["ListNode"] = None

    def append(self, value: int) -> None:
        """
        Inserts a new node at the end of the list
        """
        new_node = ListNode(value)

        if not self.head:
            self.head = new_node
            return

        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def insert(self, position: int, value: int):
        """
        Inserts data at the specified index
        """
        if position < 0:
            raise IndexError("Position cannot be negative")

        new_node = ListNode(value)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        prev = self.head
        prev_position = 0

        while prev and prev_position < position - 1:
            prev = prev.next
            prev_position += 1

        if not prev:
            raise IndexError("Position out of bounds")

        new_node.next = prev.next
        prev.next = new_node

    def remove(self, position: int) -> None:
        """
        Removes the node at the specified index
        """
        if not self.head:
            raise IndexError("Cannot remove from an empty list")
        if position < 0:
            raise IndexError("Position cannot be negative")

        if position == 0:
            self.head = self.head.next
            return

        prev = self.head
        prev_position = 0
        while prev and prev_position < position - 1:
            prev = prev.next
            prev_position += 1

        if not prev or not prev.next:
            raise IndexError("Position out of bounds")

        prev.next = prev.next.next

    def traversal(self):
        """
        Traverses the list and returns a string representation 
        """
        elements = []
        curr = self.head
        while curr:
            elements.append(str(curr.val))
            curr = curr.next

        return " -> ".join(elements)
