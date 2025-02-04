class Stack:
    def __init__(self):
        self.list_stack = []

    def __str__(self):
        values = [str(x) for x in reversed(self.list_stack)]
        return '\n'.join(values)

    def push(self, value):
        self.list_stack.append(value)
        print(f"Element {value} has been successfully inserted")

    def is_empty(self):
        if self.list_stack == []:
            print("The stack is empty")
            return True

        else:
            print("Stack contains some elements.")
            return False

    def pop(self):
        if self.is_empty():
            print("Stack is no empty")
        else:
            removed_element = self.list_stack.pop()
            print(f"Element {removed_element} has been removed from the stack.")

    def peak(self):
        if self.is_empty():
            return None
        else:
            return self.list_stack[-1]


class MinMaxStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.max_stack = []

    def peek(self):
        if not self.stack:
            raise IndexError("peek from empty stack")
        else:
            return self.stack[-1]

    def pop(self):
        if not self.stack:
            raise IndexError("peek from empty stack")
        value = self.stack.pop()
        # # If the popped value is the minimum or maximum, pop from respective stacks
        if value == self.min_stack[-1]:
            self.min_stack.pop()
        if value == self.max_stack[-1]:
            self.max_stack.pop()
        return value

    def push(self, number):
        # append on stack
        self.stack.append(number)
        if not self.min_stack or number <= self.min_stack[-1]:
            self.min_stack.append(number)
        if not self.max_stack or number >= self.max_stack[-1]:
            self.max_stack.append(number)

    def getMin(self):
        if not self.min_stack:
            raise IndexError("peek from empty min_stack")

        return self.min_stack[-1]

    def getMax(self):
        if not self.max_stack:
            raise IndexError("peek from empty max_stack")

        return self.max_stack[-1]


if __name__ == '__main__':
    stack = Stack()
    print(stack.is_empty())
    stack.push(2)
    stack.push(44)
    stack.push(3)
    stack.push(2)
    stack.push(10)
    print(stack)
    stack.pop()
    stack.pop()
    print(stack)
