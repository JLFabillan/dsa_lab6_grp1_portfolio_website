class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = None
        self.right = None
    
    def get_node_to_dict(self): # For website visualization
        return {
            "data": self.data,
            "left": self.left.get_node_to_dict() if self.left else None,
            "right": self.right.get_node_to_dict() if self.right else None
        }

class BinaryTree:
    def __init__(self, root_data=None):
        self.root = Node(root_data) if root_data is not None else None

    def insert_left(self):
        pass

    def insert_right(self):
        pass

    def postorder_traversal(self):
        pass

    def search(self):
        pass

    def delete_node(self):
        pass

    def get_tree_to_dict(self): # For website visualization
        return self.root.to_dict() if self.root else None
