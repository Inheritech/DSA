class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next
        self.prev = None
    
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
        
    def __str__(self):
        return " -> ".join([str(n) for n in self])

    def __len__(self):
        length = 0
        for n in self:
            length += 1
        return length

    def add(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        return self.tail

    def push(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        return self.head

def generate_linked_list(n, min_value, max_value):
    import random
    result_list = LinkedList()
    for i in range(n):
        result_list.add(random.randint(min_value, max_value))
    return result_list