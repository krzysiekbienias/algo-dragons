import math
from typing import List
from collections import deque


# Suitable for AlgoExpert
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# ╔════════════════════════════════════════════════════════════════════╗
# ║                          DFS traversal                             ║
# ╚════════════════════════════════════════════════════════════════════╝
def inorder(tree, array=None) -> List[int]:
    # INORDER means that root is IN
    if array is None:
        array = []
    if tree is not None:
        inorder(tree.left, array)  # Visit left subtree
        array.append(tree.value)
        inorder(tree.right, array)
    return array


def preorder(tree, array=None) -> List[int]:
    # PREORDER root first
    if array is None:
        array = []
    if tree is not None:
        array.append(tree.value)
        preorder(tree.left, array)
        preorder(tree.right, array)
    return array


def postorder(tree, array=None) -> List[int]:
    if array is None:
        array = []
    if tree is not None:
        postorder(tree.left, array)
        postorder(tree.right, array)
        array.append(tree.value)
    return array


# ════════════════════════ End of DFS traversal ════════════════════════

# ╔════════════════════════════════════════════════════════════════════╗
# ║                          BFS traversal                             ║
# ╚════════════════════════════════════════════════════════════════════╝
def bfs(root: BinaryTree) -> List:
    """
    Performs a breadth-first search (BFS) traversal on a binary tree and
    returns a list of values in level-order.

    This traversal visits nodes level by level from top to bottom, left to right.

    Parameters:
        root (BinaryTree): The root node of the binary tree.

    Returns:
        List: A list of node values in the order they are visited.

    Example:
        Given the binary tree:

                1
               / \
              2   3
             / \
            4   5

        bfs(root) → [1, 2, 3, 4, 5]

    Notes:
        - This implementation uses a queue (`collections.deque`) to process nodes level by level.
        - If the tree is empty, it returns an empty list.
        """
    if not root:
        return []
    queue = deque([root])
    result = []
    while queue:
        node = queue.popleft()
        result.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


# ════════════════════════ End of BFS traversal ════════════════════════


# ╔════════════════════════════════════════════════════════════════════╗
# ║                          Branch Sums — AlgoExpert                  ║
# ╚════════════════════════════════════════════════════════════════════╝
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


# ════════════════════════ End of Branch Sums Section ════════════════════════


# ╔════════════════════════════════════════════════════════════════════╗
# ║                          Node Depths — AlgoExpert                  ║
# ╚════════════════════════════════════════════════════════════════════╝
def node_depths(root: BinaryTree, depth=0) -> int:
    if not root:
        return 0
    return depth + node_depths(root.left, depth + 1) + node_depths(root.right, depth + 1)


# ════════════════════════ End of Node Depth ════════════════════════


# ╔════════════════════════════════════════════════════════════════════╗
# ║                         Evaluate Expression — AlgoExpert           ║
# ╚════════════════════════════════════════════════════════════════════╝
def evaluate_expression_tree(tree: BinaryTree) -> int:
    if not tree:
        return 0
    if not tree.left and not tree.right:
        return tree.value
    left_value = evaluate_expression_tree(tree.left)
    right_value = evaluate_expression_tree(tree.right)
    if tree.value == -1:
        return left_value + right_value
    if tree.value == -2:
        return left_value - right_value
    if tree.value == -4:
        return left_value * right_value
    if tree.value == -3:
        return math.floor(left_value / right_value)


# ════════════════════════ End of Evaluate Expression ════════════════════════


# ╔════════════════════════════════════════════════════════════════════╗
# ║                         Symmetrical Tree — AlgoExpert                     ║
# ╚════════════════════════════════════════════════════════════════════╝
def is_mirror(bt1: BinaryTree, bt2: BinaryTree) -> bool:
    # both nodes are None
    if not bt1 and not bt2:
        return True
    # if one node is None, the tree cannot be symmetrical
    if not bt1 or not bt2:
        return False
    return (bt1.value == bt2.value and is_mirror(bt1.left, bt2.right)  #outer children
            and is_mirror(bt1.right, bt2.left))  #iiner children


def symmetrical_tree(tree: BinaryTree):
    if not tree:
        return True
    return is_mirror(tree.left, tree.right)


# ════════════════════════ End of Symmetrical Tree ════════════════════════


# ╔════════════════════════════════════════════════════════════════════╗
# ║                         Invert Binary Tree — AlgoExpert            ║
# ╚════════════════════════════════════════════════════════════════════╝

def invert_binary_tree(tree):
    """
        Inverts (or mirrors) a binary tree in place.

        This function swaps the left and right children of every node in the tree
        recursively, resulting in a mirror image of the original tree.

        The inversion is done using a depth-first traversal (pre-order), where each node's
        children are swapped before the recursive calls are made on them.

        Parameters:
            tree (Node): The root node of the binary tree to be inverted.

        Returns:
            Node: The root of the inverted binary tree.

        Example:
            Original Tree:
                    1
                   / \
                  2   3
                 / \
                4   5

            After inversion:
                    1
                   / \
                  3   2
                     / \
                    5   4

        Notes:
            - This is a classic recursive problem.
            - The base case is when the current node is None.
            - In-place inversion means we don’t allocate new nodes; we simply mutate the pointers.
        """

    if tree is None:
        return None
    tree.left, tree.right = tree.right, tree.left
    invert_binary_tree(tree.left)
    invert_binary_tree(tree.right)
    return tree


# ════════════════════════ End of Invert Binary Tree ════════════════════════

# ╔════════════════════════════════════════════════════════════════════╗
# ║                      Binary Tree Diameter — AlgoExpert             ║
# ╚════════════════════════════════════════════════════════════════════╝
def binary_tree_diameter(tree):
    """
    Calculates the diameter of a binary tree.

    The diameter is defined as the length (in number of edges) of the longest path
    between any two nodes in the tree. This path may or may not pass through the root.

    The algorithm uses a depth-first search (DFS) approach to calculate the height of
    each subtree and keeps track of the maximum diameter encountered during traversal.

    Returns:
        int: The maximum diameter (i.e., number of edges) between any two nodes.

    Explanation of `+2` in diameter calculation:
        At any given node, the diameter passing through that node is the sum of the
        height of its left subtree and the height of its right subtree, plus 2 edges:
        - One edge to connect the current node to its left child
        - One edge to connect the current node to its right child

        For example, given this tree:

              A
             / \
            B   C

        - Height of B = 0 (leaf node)
        - Height of C = 0 (leaf node)
        - Diameter through A = 0 (left) + 0 (right) + 2 = 2

        The longest path here is: B → A → C (which has 2 edges), so +2 is necessary.
        """
    max_diameter = 0

    def _dfs(tree):
        nonlocal max_diameter  # IMPORTANT
        if tree is None:
            return -1
        left = _dfs(tree.left)  # left is the height of left subtree
        right = _dfs(tree.right)  # right is the height of right subtree
        max_diameter = max(max_diameter, left + right + 2)  # why wee need 2, draw a simple tree with 3 nodes and what
        # would bethe diameter of the tree through the root.
        return 1 + max(left, right)

    _dfs(tree)
    return max_diameter


# ════════════════════════ End of Invert Binary Tree ════════════════════════

def merge_binary_trees(tree1: BinaryTree, tree2: BinaryTree) -> "BinaryTree"|None:
    """
        Merges two binary trees by summing overlapping node values and combining structure.

        For each corresponding node in tree1 and tree2:
            - If both nodes exist, their values are summed and stored in tree1.
            - If only one of the nodes exists, it is used directly in the resulting tree.
            - The merge is done recursively for left and right children.

        This function mutates and returns `tree1` as the merged result.

        Parameters:
            tree1 (BinaryTree): The first binary tree (base tree, will be modified in-place).
            tree2 (BinaryTree): The second binary tree (merged into tree1).

        Returns:
            BinaryTree: The root of the merged binary tree.

        Example:
            Input trees:

                Tree 1:          Tree 2:
                  1                2
                 / \              / \
                3   2            1   3
               /
              5

            Merged Tree:
                  3
                 / \
                4   5
               /
              5

        Notes:
            - This implementation modifies `tree1` in place.
            - If you need to preserve both trees, create a deep copy of `tree1` before merging.
        """
    if tree1 is None:
        return tree2
    if tree2 is None:
        return tree1
    tree1.value += tree2.value
    tree1.left = merge_binary_trees(tree1.left, tree2.left)
    tree1.right = merge_binary_trees(tree1.right, tree2.right)
    return tree1


if __name__ == '__main__':
    bt1 = BinaryTree(5)
    bt1.left = BinaryTree(2)
    bt1.right = BinaryTree(3)
    bt1.left.left = BinaryTree(4)
    bt1.left.right = BinaryTree(5)
    bt1.right.left = BinaryTree(6)
    bt1.right.right = BinaryTree(7)
