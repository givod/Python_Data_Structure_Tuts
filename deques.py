class Deque:
    def __init__(self):
        self.items = []

    def add_front(self, item):
        """0(n)"""
        self.items.insert(0, item)

    def add_rear(self, item):
        """0(1)"""
        self.items.append(item)

    def remove_front(self):
        """0(n)"""
        if self.items:
            return self.items.pop(0)
        return None

    def remove_rear(self):
        """0(1)"""
        if self.items:
            return self.items.pop()
        return None

    def peek_front(self):
        if self.items:
            return self.items[0]
        return None

    def peek_rear(self):
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []

    def list_items(self):
        return self.items



    def check_palindrome(self, input_str):

        if input_str:
            return False
            
        my_deque = Deque()
        for char in input_str:
            my_deque.add_rear(char)

        while my_deque.size() >= 2:
            front_item = my_deque.remove_front()
            rear_item = my_deque.remove_rear()

            if front_item != rear_item:
                return False

        return True
