class Node:
    """Node structure for the binary tree"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    """Binary tree data structure"""
    def __init__(self):
        self.root = None
    
    def insert_root(self, value):
        """Insert node as a root"""
        self.root = Node(value)

    def insert_left(self, target_node, value):
        """Insert node to the left of a target node"""
        if self.root is None:
            # Tree is empty
            # Node will become the root
            self.insert_root(value)
        if target_node is None:
            # Target does not exist
            return
        if target_node.left is None:
            # Can insert node to the left of target
            target_node.left = Node(value)
        else:
            # Target already has node to the left
            # Push existing left node to lower level
            node_to_insert = Node(value)
            node_to_insert.left = target_node.left
            target_node.left = node_to_insert

    def insert_right(self, target_node, value):
        """Insert node to the right of a target node"""
        if self.root is None:
            # Tree is empty
            # Node will become the root
            self.insert_root(value)
        if target_node is None:
            # Target does not exist
            return
        if target_node.right is None:
            # Can insert node to the right of target
            target_node.right = Node(value)
        else:
            # Target already has node to the right
            # Push existing right node to lower level
            node_to_insert = Node(value)
            node_to_insert.right = target_node.right
            target_node.right = node_to_insert

    def postorder_traversal(self, start, traversal):
        """Traverse the tree in postorder (left, right, root)"""
        if start:
            traversal = self.postorder_traversal(start.left,traversal)
            traversal = self.postorder_traversal(start.right,traversal)
            traversal += (str(start.value) + " ")
        return traversal

    def search(self, value):
        """Returns the node if in tree"""
        return self.postorder_search(self.root, value)

    def postorder_search(self, target, value):
        """Search the tree using postorder traversal"""
        if target is None:
            # Tree is empty
            return None
        
        # Search left
        left_node = self.postorder_search(target.left, value)
        if left_node:
            return left_node
        
        # Search right
        right_node = self.postorder_search(target.right, value)
        if right_node:
            return right_node
        
        # Search node
        if target.value == value:
            return target
        
        return None

    def find_deepest_node(self):
        if not self.root:
            return None
        
        queue = [self.root]
        last = None

        while queue:
            last = queue.pop(0)
            if last.left:
                queue.append(last.left)
            if last.right:
                queue.append(last.right)
        
        return last

    def delete_deepest_node(self, deepest):
        queue = [self.root]

        while queue:
            node = queue.pop(0)

            if node.left:
                if node.left == deepest:
                    node.left = None
                    return
                queue.append(node.left)

            if node.right:
                if node.right == deepest:
                    node.right = None
                    return
                queue.append(node.right)

    def delete_node(self, value):
        if self.root is None:
            return False

        if self.root.value == value and not self.root.left and not self.root.right:
            self.root = None
            return True

        target = self.search(value)
        if target is None:
            return False

        deepest = self.find_deepest_node()

        target.value = deepest.value

        self.delete_deepest_node(deepest)

        return True
