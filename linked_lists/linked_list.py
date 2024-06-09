class Node:
    def __init__(self, val) -> None:
        """
        Description
        -----------
        Node object for linked list

        Parameters
        ----------
        val : int
        """

        self.val = val
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
        temp_node=self.head
        result=''
        while temp_node is not None:
            result=str(temp_node.value)
            if temp_node.next is not None:
                result+=' -> '
            temp_node=temp_node.next
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

    def prepend(self,value:int):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1


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



    print("the end")
