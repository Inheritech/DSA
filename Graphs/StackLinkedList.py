from LinkedList import Node

class Stack:
    def __init__(self, limit = -1):
        self.head = None
        self.limit = limit
        self.size = 0

    def __str__(self):
        values = []
        node = self.head
        while node:
            values.append(str(node))
            node = node.next
        values.reverse()
        return " -> ".join(values)

    def is_empty(self):
        return self.size == 0

    def push(self, value):
        if self.size == self.limit:
            return
        node = Node(value)
        if self.head is not None:
            node.next = self.head
        self.head = node
        self.size += 1

    def pop(self):
        if self.size == 0:
            return None
        value = self.head.value
        self.head = self.head.next
        self.size -= 1
        return value

    def peek(self):
        if self.size == 0:
            return None
        return self.head.value
    
    def clear(self):
        if self.size == 0:
            return
        self.head = None

if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack)
    stack.push(4)
    print(stack)
    print(stack.pop())
    print(stack)
    print(stack.peek())
    print(stack)