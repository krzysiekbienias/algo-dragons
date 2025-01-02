import math
from typing import List
from collections import deque

# Suitable for AlgoExpert
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def dfs_preorder(root: BinaryTree) -> List:
    if not root:
        return []
    return [root.value] + dfs_preorder(root.left) + dfs_preorder(root.right)


def dfs_inorder(root: BinaryTree) -> List:
    if not root:
        return []
    return dfs_inorder(root.left) + [root.value] + dfs_inorder(root.right)


def dfs_postorder(root: BinaryTree) -> List:
    if not root:
        return []
    return dfs_postorder(root.left) + dfs_postorder(root.right) + [root.value]

def bfs(root: BinaryTree) -> List:
    if not root:
        return []
    queue = deque([root])
    result=[]
    while queue:
        node = queue.popleft()
        result.append(node.value)
        if node.left:
            queue.append(node.left)
        elif node.right:
            queue.append(node.right)
    return result

# Branch Sums AlgoExpert
def dfs(root: BinaryTree, running_sum, sum_per_branch) -> List | None:
    if not root:
        return
    new_sum = running_sum + root.value
    if not root.left and not root.right:
        sum_per_branch.append(new_sum)
        return
    dfs(root.left, new_sum, sum_per_branch)
    dfs(root.right, new_sum, sum_per_branch)


def branch_sums(root: BinaryTree) -> List:
    brunch_sums = []
    dfs(root, 0, brunch_sums)
    return brunch_sums

 # Node Depths AlgoExpert
 def node_depths(root: BinaryTree,depth=0) -> int:
     if not root:
         return 0
     return depth+node_depths(root.left,depth+1)+node_depths(root.right,depth+1)

 # Evaluate Expression Tree
 def evaluate_expression_tree(tree: BinaryTree) -> int:
     if not tree:
         return 0
     if not tree.left and not tree.right:
         return tree.value
     left_value = evaluate_expression_tree(tree.left)
     right_value = evaluate_expression_tree(tree.right)
     if tree.value==-1:
         return left_value + right_value
     if tree.value==-2:
         return left_value - right_value
     if tree.value==-4:
         return left_value * right_value
     if tree.value==-3:
         return math.floor(left_value / right_value)





if __name__ == '__main__':
    bt1 = BinaryTree(5)
    bt1.left = BinaryTree(2)
    bt1.right = BinaryTree(3)
    bt1.left.left = BinaryTree(4)
    bt1.left.right = BinaryTree(5)
    bt1.right.left = BinaryTree(6)
    bt1.right.right = BinaryTree(7)
