class Node:
    def __init__(self,val,next=None) -> None:
        
        self.val=val
        self.next=next



class LinkedList:
    def __init__(self,value) -> None:
        
        new_node=Node(value)

        self.head=new_node
        self.tail=new_node

        self.length=1

    def print_linked_list(self):
        temp=self.head
        while self.head is not None:
            print(str(temp.val)+"->")
            temp=temp.next

my_ll=LinkedList(4)
my_ll.tail.next=Node(5)
my_ll.tail=Node(5)
my_ll.length+=1
my_ll.tail.next=Node(8)
my_ll.tail=Node(8)
my_ll.length+=1
my_ll.tail.next=Node(11)
my_ll.tail=Node(11)
my_ll.length+=1
my_ll.tail.next=Node(47)
my_ll.tail=Node(47)
my_ll.length+=1


print("the end")
    