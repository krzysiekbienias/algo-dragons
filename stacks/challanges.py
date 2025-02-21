from stack_list import Stack


# from AlgoExper
def balanced_brackets(string):
    brackets = set(['(', ')', '[', ']', '{', '}'])
    brackets_map = {'(': ')', '[': ']', '{': '}'}
    open_brackets = ['(', '[', '{']
    stack = []
    for ch in string:
        if ch not in brackets:
            continue
        if ch in open_brackets:
            stack.append(ch)
        elif stack and ch == brackets_map[stack[-1]]:
            stack.pop()
        else:
            return False
    return len(stack) == 0


#from Boot.Dev - simpler version
def is_balanced(input_str):
    if len(input_str) == 0:
        return True
    stack_ob = Stack()
    for ch in input_str:
        if ch == '(':
            stack_ob.push(ch)
        elif stack_ob.list_stack and  ch == ')':
            stack_ob.pop()
        else:
            return False # if we have ) for empty stack
    return len(stack_ob.list_stack) == 0


if __name__ == "__main__":
    is_balanced('())(()')
