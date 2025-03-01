class PriorityQueue:
    def __init__(self):
        self.elements = []
    """
    A simple implementation of a priority queue.

    This class provides a way to manage a collection of elements,
    each associated with a priority. Elements with lower priority
    values are dequeued before those with higher priority values.

    Attributes
    ----------
    elements : list
        A list that holds the tuples of (priority, item),
        maintaining the order of insertion.

    Methods
    -------
    empty() -> bool
        Checks if the priority queue is empty.

    push(priority: int, item) -> None
        Adds an item to the priority queue with the given priority.

    pop() -> any
        Removes and returns the item with the highest priority 
        (i.e., the lowest priority number). If the queue is empty, 
        returns None.
    """

    def empty(self)->bool:
        """Check if the priority queue is empty.

        Returns
        -------
        bool
            True if the queue is empty, False otherwise.
        """
        if self.elements:
            return False
        else:
            return True

    def push(self, priority, item):
        """Add an item to the priority queue with the specified priority.

        Parameters
        ----------
        priority : int
            The priority of the item. Lower values indicate higher priority.
        item : any
            The item to be added to the priority queue.
        """
        self.elements.append((priority, item))

    def pop(self):
        """Remove and return the item with the highest priority.
        Returns
        -------
        any
            The item with the highest priority (lowest priority number),
            or None if the queue is empty.
        """
        if self.empty():
            return None
        min_index_so_far = 0  # it will keep track of the index of tuple
        for i in range(len(self.elements)):
            if self.elements[i][0] < self.elements[min_index_so_far][0]:
                min_index_so_far = i
        min_index_value = self.elements[min_index_so_far][1]
        del self.elements[min_index_so_far]
        return min_index_value


if __name__ == "__main__":
    pq = PriorityQueue()
    pq.push(7, "Kingsroad")
    pq.push(5, "Godsway")
    pq.push(2, "East Pass")
    pq.push(10, "Bunscha")
    pq.pop()
