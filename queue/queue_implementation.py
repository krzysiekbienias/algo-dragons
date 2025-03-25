from collections import deque


class QueuePushInFavourite:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            return self.items.pop(0)  # this operation is O(n)!!
        else:
            raise IndexError('Pop from an empty queue')

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)


class QueuePopInFavourite:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0, item)  # this operation is O(n)

    def pop(self):
        if not self.items:
            return self.items.pop
        else:
            raise IndexError('Pop from an empty queue')

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


# the most efficient implementation uses deque


