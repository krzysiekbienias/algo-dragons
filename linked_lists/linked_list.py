from typing import Any
from graphviz import Digraph
from IPython.display import display
import numpy as np


class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value: int | None = None):
        self.head = Node(value) if value is not None else None  # Maintain a `head` pointer

    def append(self, value: int):
        if not self.head:
            self.head = Node(value)
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = Node(value)

    def is_empty(self):
        """Returns True if the linked list is empty, otherwise False."""
        return self.head is None

    def remove_tail(self):
        if not self.head or not self.head.next:
            self.head = None  # If only one node, set head to None
            return

        current = self.head
        while current.next and current.next.next:
            current = current.next

        current.next = None  # Remove tail

    def remove_head(self):
        if not self.head or not self.head.next:
            self.head = None  # If only one node, set head to None
            return

        self.head = self.head.next  # Update head reference

    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next  # Store next node
            current.next = prev  # Reverse the link
            prev = current  # Move prev forward
            current = next_node  # Move current forward

        self.head = prev

    def visualize(self):
        """Displays a Graphviz visualization of the linked list inline in Jupyter."""
        dot = Digraph()
        dot.attr(rankdir="LR")
        current = self.head
        visited = set()  # To avoid infinite loops in case of cycles
        while current:
            if id(current) in visited:  # Detect cycles
                break
            visited.add(id(current))

            dot.node(str(id(current)), str(current.value))
            if current.next:
                dot.edge(str(id(current)), str(id(current.next)))  # Connect to next node
            else:
                dot.node("None", "None", shape="plaintext")  # Create None node
                dot.edge(str(id(current)), "None")  # Last node points to None
            current = current.next

        display(dot)


class LinkedListTwoPointers:

    def __init__(self):
        """
        Description
        -----------
        Linked list without any Node.
        """
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next

        return result

    def append(self, value: int):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value: int):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def traverse(self) -> None:
        """
        Description
        -----------
        Traverse the linked list
        Returns
        -------
        None

        """
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def search(self, target: int) -> bool:
        """
        Description
        -----------
        Checks if a value is present in the linked list.

        Parameters
        ----------
        target

        Returns
        -------
        bool

        """
        temp = self.head
        while temp is not None:
            if temp.value == target:
                return True

        return False

    def get_value(self, index: int) -> Node | None:
        """
        Description
        -----------
        Get the Node at the given index.

        Parameters
        ----------
        index:int

        Returns
        -------
        None
        """
        if index == -1:
            return self.tail
        if index < -1 or index > self.length:
            return None
        current: Node = self.head
        for _ in range(index):
            current = current.next
        return current

    def set_value(self, index: int, new_value: int):
        temp_node = self.get_value(index)
        if temp_node:
            temp_node.value = new_value
        else:
            return None

    def generate(self, n: int, min_value: int, max_value: int):
        self.head = None
        self.tail = None
        for i in range(n):
            self.append(np.random.randint(min_value, max_value))
        return self

    def remove_all(self):
        self.head = None
        self.tail = None
        self.length = 0


# is it also annother approach where linked ist is constructed and manipulated by managing nodes directly


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(3)

    print(linked_list)
    linked_list.set_value(1, 22)
    print(linked_list)

    custom_list = LinkedList()
    custom_list.generate(10, 1, 100)
    print(custom_list)

    print("the end")
