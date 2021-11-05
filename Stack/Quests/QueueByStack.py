from StackOfPlates import Stack

class QueueByStack:
    def __init__(self):
        self.inStack = Stack()
        self.outStack = Stack()

    def enqueue(self, value):
        while not self.outStack.is_empty():
            self.inStack.push(self.outStack.pop())
        self.inStack.push(value)

    def dequeue(self):
        while not self.inStack.is_empty():
            self.outStack.push(self.inStack.pop())
        if self.outStack.is_empty():
            return None
        return self.outStack.pop()

if __name__ == '__main__':
    queueStack = QueueByStack()
    for i in range(3):
        queueStack.enqueue(i)
    for i in range(3):
        print(queueStack.dequeue())    