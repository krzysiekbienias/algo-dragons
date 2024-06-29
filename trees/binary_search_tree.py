from binarytree import tree
import graphviz

class BSTNode:
    def __init__(self,value,left_child=None,right_child=None) -> None:
        self.value=value
        self.left_child=left_child
        self.right_child=right_child


class BinarySearchTree:
    """ class BinarySearchTree

    Initialise empty binary search tree.
    """
    def __init__(self) -> None:
        self.root=None

    def insert(self,value:int):
        new_node=BSTNode (value)
        if self.root is None:
            self.root=new_node
            return True
        temp=self.root # assigne root to temp
        while True:
            if new_node.value==temp.value:
                return False
            if new_node.value<temp.value:
                if temp.left is None:
                    temp.left=new_node 
                    return True
                temp=temp.left 
            
            if new_node.value>temp.value:
                if temp.right is None:
                    temp.right=new_node
                    return True
                temp=temp.right





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

        

        


nodes=[7,18,56,23,44,25,26]
my_tree=BinarySearchTree()
for n in nodes:
    my_tree.insert(n)

visualize_binary_tree(my_tree)

print("print the end")




