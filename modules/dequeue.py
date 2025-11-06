class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class DeQueue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self, data):
        # add data to rear
        pass

    def enqueue_front(self, data):
        # add data to front
        pass

    def dequeue(self):
        # remove data from front
        pass

    def dequeue_rear(self):
        # remove data from rear
        pass