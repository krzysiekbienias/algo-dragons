from typing import Any

import numpy as np

np.random.seed(5)


class Node:
    def __init__(self, value) -> None:
        """
        Description
        -----------
        Node object for linked list

        Parameters
        ----------
        value : int
        """

        self.value = value
        self.next = None


class LinkedList:

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


class LinkedListWithOneNode:

    def __init__(self, value) -> None:
        """

        Parameters
        ----------
        value :
        """

        new_node = Node(value)

        self.head = new_node
        self.tail = new_node

        self.length = 1

    def print_linked_list(self):
        temp = self.head
        while self.head is not None:
            print(str(temp.val) + "->")
            temp = temp.next

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
