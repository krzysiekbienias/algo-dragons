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

    def get(self, index: int) -> Node:
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
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value

    def set_value(self):
        pass


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


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(3)

    print(linked_list)
    print(linked_list.head.value)
    print(linked_list.tail.value)
    linked_list.traverse()

    print("the end")
