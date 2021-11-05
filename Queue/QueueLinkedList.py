from LinkedList import LinkedList

class Queue:
    def __init__(self):
        self.list = LinkedList()
        self.length = 0

    def __str__(self):
        return str(self.list)

    def __len__(self):
        return self.length

    def enqueue(self, value):
        self.list.add(value)
        self.length += 1

    def dequeue(self):
        if self.list.head is None:
            return None
        node = self.list.head
        self.list.head = node.next
        self.length -= 1
        return node.value
    
    def peek(self):
        if self.list.head is None:
            return None
        return self.list.head.value

    def isEmpty(self):
        return self.length == 0

if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue)
    print(len(queue))
    print(queue.dequeue())
    print(queue)