class Stack:
    def __init__(self, limit = -1):
        self.list = []
        self.limit = limit

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    def isEmpty(self):
        return len(self.list) == 0

    def isFull(self):
        return len(self.list) == self.limit

    def push(self, value):
        if len(self.list) == self.limit:
            return # Might want to raise an error
        self.list.append(value)
    
    def pop(self):
        if self.isEmpty():
            return None
        return self.list.pop()

    def peek(self):
        return self.list[-1]

    def clear(self):
        self.list = []
