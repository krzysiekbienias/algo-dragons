from  graphviz import Digraph


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
            if value < current_node.value:
                if current_node.left is None:
                    current_node.left = BST(value)
                    break
                else:
                    current_node = current_node.left # move to the left child
            else:
                if current_node.right is None:
                    current_node.right = BST(value)
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

    def visualize(self):
        """Returns a string representation of the tree with branches."""
        lines, *_ = self._visualize(self)
        return '\n'.join(lines)

    def _visualize(self, node):
        """Helper function to visualize the tree."""
        if node is None:
            return ["", 0, 0]  # No node

        # Convert the left and right subtrees into a list of strings
        left_lines, left_pos, left_width = self._visualize(node.left)
        right_lines, right_pos, right_width = self._visualize(node.right)

        # Current node's value as a string
        node_value = str(node.value)
        node_width = len(node_value)

        # Create the current line representation
        if left_width > 0:
            # Connect the left child
            connector_left = ' ' * (left_pos + 1) + '/'
        else:
            connector_left = ''

        if right_width > 0:
            # Connect the right child
            connector_right = ' ' * (node_width + left_width + 1) + '\\'
        else:
            connector_right = ''

        # Current level of the tree
        current_line = ' ' * left_pos + node_value + ' ' * (right_pos - left_pos - node_width + 1)

        lines = [current_line] + [connector_left, connector_right] + left_lines + right_lines

        # Calculate new positions and widths for child nodes
        new_pos = (left_width + right_pos + node_width) // 2
        return lines, new_pos, node_width + left_width + right_width

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


    def visualize(self, dot=None):
        """Visualize the tree using Graphviz with clear left/right child indication.
        Reocemeded to run this
        """
        if dot is None:
            dot = Digraph()

        dot.node(str(self.value), str(self.value))  # Create the node

        # If there's a left child, add an explicit left direction
        if self.left:
            dot.edge(str(self.value), str(self.left.value), label="L", tailport="sw", headport="n")
            self.left.visualize(dot)

        # If there's a right child, add an explicit right direction
        if self.right:
            dot.edge(str(self.value), str(self.right.value), label="R", tailport="se", headport="n")
            self.right.visualize(dot)

        return dot


if __name__ == '__main__':
    # Create a BST and insert values using the new method
    root = BST(10)
    root.left = BST(5)
    root.left.left = BST(2)
    root.left.left.left = BST(1)
    root.left.right = BST(7)
    root.right = BST(15)
    root.right.left = BST(13)
    root.right.left.right = BST(14)
    root.right.right = BST(22)
    root.insert(12)

    # Generate the Markdown representation of the BST
    tree_representation = root.visualize()

    # Print the result for Markdown
    print("# Binary Search Tree Visualization\n")
    print( tree_representation )



