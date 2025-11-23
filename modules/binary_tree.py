class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = None
        self.right = None
    
    def get_node_to_dict(self): # For website visualization
        return {
            "value": self.value,
            "left": self.left.get_node_to_dict() if self.left else None,
            "right": self.right.get_node_to_dict() if self.right else None
        }

class BinaryTree:
    def __init__(self, root_value=None):
        self.root = Node(root_value) if root_value is not None else None

    def insert_left(self, current_node, value):
        if current_node.left is None:
            current_node.left = Node(value)
        else:
            new_node = Node(value)
            new_node.left = current_node.left
            current_node.left = new_node

    def insert_right(self, current_node, value):
        if current_node.right is None:
            current_node.right = Node(value)
        else:
            new_node = Node(value)
            new_node.right = current_node.right
            current_node.right = new_node

    def postorder_traversal(self, start, traversal):
        if start:
            traversal = self.postorder_traversal(start.left,traversal)
            traversal = self.postorder_traversal(start.right,traversal)
            traversal += (str(start.value) + " ")
        return traversal

    def search(self):
        pass

    def delete_node(self):
        pass

    def get_tree_to_dict(self): # For website visualization
        return self.root.to_dict() if self.root else None
