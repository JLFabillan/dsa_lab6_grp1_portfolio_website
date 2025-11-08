class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class Deque:
    def __init__(self):
        self.front = None
        self.rear = None

    def insert_left(self, value):
        new_node = Node(value)

        if self.front is None:  # deque empty
            self.front = self.rear = new_node
            return

        new_node.next = self.front
        self.front.prev = new_node
        self.front = new_node

    def insert_right(self, value):
        new_node = Node(value)

        if self.rear is None:  # deque empty
            self.front = self.rear = new_node
            return

        self.rear.next = new_node
        new_node.prev = self.rear
        self.rear = new_node

    def remove_left(self):
        if self.front is None:
            return None

        removed_data = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None  # deque becomes empty
        else:
            self.front.prev = None

        return removed_data

    def remove_right(self):
        if self.rear is None:
            return None

        removed_data = self.rear.data
        self.rear = self.rear.prev

        if self.rear is None:
            self.front = None  # deque becomes empty
        else:
            self.rear.next = None
        
        return removed_data

    def get_items(self):  # return list of values (for html display)
        items = []
        current = self.front
        while current:
            items.append(current.data)
            current = current.next
        return items