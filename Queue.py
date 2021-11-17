class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """0(n)"""
        self.items.insert(0, item)

    def dequeue(self):
        """0(1)"""
        if self.items:
            return self.items.pop()
        return None

    def peek(self):
        """0(1)"""
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        """0(1)"""
        return len(self.items)

    def is_empty(self):
        """0(1)"""
        return self.items == []


