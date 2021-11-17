class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        """ The runtime for this method is 0(1), constant time"""
        self.items.append(item)

    def pop(self):
        """ The runtime is constant time"""
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



def match_symbols(symbol_str):

    symbol_pairs = {
        '(':')',
        '[':']',
        '{':'}'
    }

    openers = symbol_pairs.keys()
    myStack = Stack()

    index = 0
    while index < len(symbol_str):
        symbol = symbol_str[index]

        if symbol in openers:
            myStack.push(symbol)
        else:
            if myStack.is_empty():
                return False
            else:
                top_item = myStack.pop()
                if symbol != symbol_pairs[top_item]:
                    return False
        index +=1
    if myStack.is_empty():
        return True

    return False

print(match_symbols('([{}])'))
print(match_symbols('(([{}]])'))