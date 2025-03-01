import random


class MinHeap:
    def push(self, value, priority=None):
        if priority is not None:
            self.elements.append((priority, value))
            self.bubble_up(index=len(self.elements) - 1)  # passing the index of the element you just append, so the
            # last one
        if priority is None:
            self.elements.append(value)
            self.bubble_up(index=len(self.elements) - 1)

    def bubble_up(self, index):
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

    def __init__(self):
        self.elements = []

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
