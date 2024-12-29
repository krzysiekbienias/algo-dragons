class Stack:
    def __init__(self):
        self.list_stack=[]

    def __str__(self):
        values=[str(x) for x in reversed(self.list_stack)]
        return '\n'.join(values)


    def push(self,value):
        self.list_stack.append(value)
        print(f"Element {value} has been successfully inserted")


    def is_empty(self):
        if self.list_stack==[]:
            print("The stack is empty")
            return True

        else:
            print("Stack contains some elements.")
            return False

    def pop(self):
        if self.is_empty():
            print("Stack is no empty")
        else:
            removed_element=self.list_stack.pop()
            print(f"Element {removed_element} has been removed from the stack.")

    def peak(self):
        if self.is_empty():
            return None
        else:
            return self.list_stack[-1]


if __name__ == '__main__':
    stack=Stack()
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
