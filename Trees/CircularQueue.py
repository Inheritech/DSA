from LinkedList import Node

class CircularQueue:
    def __init__(self, limit):
        self.head = None
        self.tail = None
        self.limit = limit
        self.length = 0

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next

    def __str__(self):
        return " -> ".join([str(n) for n in self])

    def __len__(self):
        return self.length

    def enqueue(self, value):
        if self.length == self.limit:
            head_node = self.head
            self.head = head_node.next
            head_node.value = value
            head_node.next = None
            self.tail.next = head_node
            self.tail = head_node
        else:
            self.length += 1
            next_node = Node(value)
            if self.head is None:
                self.head = next_node
                self.tail = next_node
            else:
                self.tail.next = next_node
                self.tail = next_node

    def dequeue(self):
        if self.head is None:
            return None
        self.length -= 1
        head_node = self.head
        self.head = head_node.next
        return head_node.value

    def peek(self):
        if self.head is None:
            return None
        return self.head.value

    def clear(self):
        self.head = None
        self.tail = None
        self.length = 0

if __name__ == '__main__':
    queue = CircularQueue(2)
    queue.enqueue(1)
    queue.enqueue(2)
    print(queue)
    queue.enqueue(3)
    print(queue)