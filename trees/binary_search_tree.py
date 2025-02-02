from binarytree import tree
import graphviz


class BSTNode:
    def __init__(self, value, left_child=None, right_child=None) -> None:
        self.value = value
        self.left_child = left_child
        self.right_child = right_child


class BinarySearchTree:
    """ class BinarySearchTree

    Initialise empty binary search tree.
    """

    def __init__(self) -> None:
        self.root = None

    def insert(self, value: int):
        new_node = BSTNode(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root  # assigne root to temp
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left

            if new_node.value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

# version used in AlgoExpert chalenges
class BST:
    """
       A class representing a node in a Binary Search Tree (BST).

       Each node contains a value and pointers to its left and right children.
    """
    def __init__(self, value:int) -> None:
        self.value=value
        self.left=None
        self.right=None

    # iterative approach
    def insert(self, value:int):
        """
       Check if a given value exists in the Binary Search Tree.

       Parameters:
           value (int): The value to search for.

       Returns:
           bool: True if the value exists in the tree, False otherwise.
        """
        current_node=self # start from root
        while True:
            if current_node.value < value:
                if current_node.left is None:
                    current_node.left = BSTNode(value)
                    break
                else:
                    current_node = current_node.left # move to the left child
            else:
                if current_node.right is None:
                    current_node.right = BSTNode(value)
                    break
                else:
                    current_node = current_node.right # move to the right child
        return self

    # iterative approach
    def contains(self, value:int) -> bool:
        current_node=self
        while current_node.value is not None:
            if value==current_node.value:
                return True
            if value<current_node.value:
                current_node = current_node.left # move to the left
            else:
                current_node = current_node.right
        return False

    # recursive approach itarative requires using Stack
    def inorder(self, tree,array):
        if tree is not None:
            self.inorder(tree.left,array) # Visit left subtree
            array.append(tree.value)
            self.inorder(tree.right,array)
        return array

    def preorder(self, tree,array):
        if tree is not None:
            array.append(tree.value)
            self.preorder(tree.left,array)
            self.preorder(tree.right,array)
        return array

    def postorder(self, tree,array):
        if tree is not None:
            self.postorder(tree.left,array)
            self.postorder(tree.right,array)
            array.append(tree.value)
        return array





def visualize_binary_tree(tree):
    dot = graphviz.Digraph()
    dot.node(str(tree.root.value))

    def add_nodes_edges(node):
        if node.left:
            dot.node(str(node.left.value))
            dot.edge(str(node.value), str(node.left.value))
            add_nodes_edges(node.left)
        if node.right:
            dot.node(str(node.right.value))
            dot.edge(str(node.value), str(node.right.value))
            add_nodes_edges(node.right)

    add_nodes_edges(tree)
    dot.render('binary_tree', view=True, format='png')


if __name__ == '__main__':
    nodes = [7, 18, 56, 23, 44, 25, 26]
    my_tree = BinarySearchTree()
    for n in nodes:
        my_tree.insert(n)

    visualize_binary_tree(my_tree)

    print("print the end")
