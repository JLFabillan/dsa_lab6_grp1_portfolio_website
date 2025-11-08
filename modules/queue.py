class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)

        if self.rear is None:  # queue is empty
            self.front = self.rear = new_node
            return
        
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return None  # queue empty

        removed_data = self.front.data
        self.front = self.front.next
        
        if self.front is None:  # reset rear if queue becomes empty
            self.rear = None

        return removed_data

    def get_items(self):  # return all values (for html display)
        items = []
        current = self.front
        while current:
            items.append(current.data)
            current = current.next
        return items