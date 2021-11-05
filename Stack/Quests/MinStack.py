from LinkedList import Node

class MinStack:
    def __init__(self):
        self.top = None
        self.minNode = None

    def __str__(self):
        values = []
        node = self.top
        while node:
            values.append(str(node))
            node = node.next
        return " -> ".join(values)

    def is_empty(self):
        return self.top is None

    def min(self):
        if self.minNode is None:
            return None
        return self.minNode.value

    def push(self, value):
        if self.minNode is None:
            self.minNode = Node(value)
        else:
            if self.minNode.value >= value:
                self.minNode = Node(value, next = self.minNode)
        self.top = Node(value, next = self.top)

    def pop(self):
        popped = self.top.value
        self.top = self.top.next
        if popped == self.minNode.value:
            self.minNode = self.minNode.next
        return popped

if __name__ == '__main__':
    stack = MinStack()
    stack.push(5)
    stack.push(3)
    stack.push(6)
    stack.push(3)
    stack.push(4)
    stack.push(1)
    stack.push(2)
    stack.push(1)
    while not stack.is_empty():
        print(stack)
        print("Min: ", stack.min())
        stack.pop()