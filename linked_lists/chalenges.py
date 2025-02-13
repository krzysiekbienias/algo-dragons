# The key takeaway is to adapt the algorithm to the specific structure you’re working with. 😊
# AlgoExpert defines LinkedList as follows :
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def create_linked_list(values):
    # Initialize the head node with the first value
    head = LinkedList(values[0])
    current = head

    # Loop through the remaining values and create subsequent nodes
    for value in values[1:]:
        new_node = LinkedList(value)
        current.next = new_node  # Link the current node to the new node
        current = new_node  # Move to the new node

    return head


def print_linked_list(linked_list):
    current = linked_list
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")


# remove duplicates from AlgoExpert
def remove_duplicates_from_linked_list(linked_list: LinkedList):
    current_node = linked_list
    while current_node is not None and current_node.next is not None:

        if current_node.value == current_node.next.value:
            current_node.next = current_node.next.next
        else:
            current_node = current_node.next
    return linked_list

def remove_kt_node_from_end(head,k):
    p1=head # i'll move p1 forward by ksteps
    p2=head
    #move p1 ksteps ahead
    for _ in range(k+1):
        if not p1:
            return head # it may happen that K is greated that or equal the lenghth of the list
        p1=p1.next
    if not p1:
        return head.next
    # move both p1 and p2 until p1 reaches the end
    while p1:
        p1=p1.next
        p2=p2.next
    p2.next=p2.next.next
    return head

# key points:
# Step 1: Move p1 K steps ahead to create the gap.
# 2.Step 2: Move both p1 and p2 together until p1 reaches the end of the list. At this point, p2 is just before
    # the node to remove.
# 3.Final Step: Set p2.next = p2.next.next to bypass the Kth node from the end and effectively remove it.




if __name__ == '__main__':
    ll1 = create_linked_list([1, 2, 2, 3, 4, 5])
    print_linked_list(ll1)
    ll2=remove_kt_node_from_end(ll1,k=2)
    print_linked_list(ll2)

