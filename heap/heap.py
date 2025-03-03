import random


class MinHeap:
    def __init__(self):
        """Initialize a new empty MinHeap.

        Attributes
        ----------
        elements: list
            A list to store the elements of the heap. Elements can be tuples with (priority, value)
            or single values.
        """
        self.elements = []


    def push(self, value, priority=None):
        """Add a new value to the heap with an optional priority.

        Parameters
        ----------
        value : any
            The value to be added to the heap.
        priority : int, optional
            The priority of the value. If None, the value is added without priority.

        Notes
        -----
        If a priority is given, the value is stored as a tuple (priority, value).
        The new element is placed in the correct position to maintain the heap property.
        """
        if priority is not None:
            self.elements.append((priority, value))
            self.bubble_up(index=len(self.elements) - 1)  # passing the index of the element you just append, so the
            # last one
        if priority is None:
            self.elements.append(value)
            self.bubble_up(index=len(self.elements) - 1)

    def bubble_up(self, index):
        """Restore the heap property by moving the element at the specified index up.

        Parameters
        ----------
        index : int
            The index of the element to bubble up.

        Notes
        -----
        This function compares the element at `index` with its parent and swaps them if necessary,
        continuing this process until the heap property is restored or the root is reached.
        """
        if index == 0:
            return

        parent_index = (index - 1) // 2

        if isinstance(self.elements[0], tuple):
            # Compare using priority for tuples
            if self.elements[index][0] < self.elements[parent_index][0]:
                self.elements[index], self.elements[parent_index] = self.elements[parent_index], self.elements[index]
                self.bubble_up(parent_index)
        else:
            # Compare using value for single values
            if self.elements[index] < self.elements[parent_index]:
                self.elements[index], self.elements[parent_index] = self.elements[parent_index], self.elements[index]
                self.bubble_up(parent_index)



    def peek(self):
        if len(self.elements) == 0:
            return None
        return self.elements[0][1]


if __name__ == "__main__":
    # [8, 10, 9, 21, 31, 27, 12, 58, 99, 42, 33, 39]
    heaped_array = [8, 10, 9, 21, 31, 27, 12, 58, 99, 42, 33, 39]

    # random.seed(42)
    # random.shuffle(heaped_array)

    mean_heap = MinHeap()
    mean_heap.push(58)
    mean_heap.push(27)
    mean_heap.push(9)
    mean_heap.push(99)
    mean_heap.push(42)
    mean_heap.push(12)
    mean_heap.push(39)
    mean_heap.push(21)
    mean_heap.push(31)
    mean_heap.push(8)
    mean_heap.push(10)
    mean_heap.push(33)
