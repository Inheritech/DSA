from LinkedList import Node

class Stack:
    def __init__(self, stack_size = -1):
        self.stack_size = stack_size
        self.length = 0
        self.top = None

    def __str__(self):
        values = []
        node = self.top
        while node:
            values.append(str(node))
            node = node.next
        return " -> ".join(values)

    def __len__(self):
        return self.length

    def push(self, value):
        if self.length == self.stack_size:
            return
        self.top = Node(value, next = self.top)
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        popped = self.top.value
        self.top = self.top.next
        self.length -= 1
        return popped

    def peek(self):
        if self.length == 0:
            return None
        return self.top.value

    def clear(self):
        self.top = None

    def is_empty(self):
        return self.length == 0

    def is_full(self):
        return self.length == self.stack_size


class SetOfStacks:
    def __init__(self, stack_size = -1):
        self.stack_size = stack_size
        self.stacks = [Stack(self.stack_size)]

    def __str__(self):
        values = [str(stack) for stack in self.stacks]
        values.reverse()
        return " -> ".join(values)

    def __len__(self):
        return len(self.stacks)

    def push(self, value):
        last_stack = self.stacks[-1]
        if last_stack.is_full():
            last_stack = Stack(self.stack_size)
            self.stacks.append(last_stack)
        last_stack.push(value)

    def pop(self):
        last_stack = self.stacks[-1]
        popped = last_stack.pop()
        if last_stack.is_empty():
            self.stacks.pop()
        return popped

    def peek(self):
        last_stack = self.stacks[-1]
        return last_stack.peek()

    def popAt(self, index):
        if index < 0 or index >= len(self.stacks):
            return None
        stack = self.stacks[index]
        if stack.is_empty():
            return None
        popped = stack.pop()
        if stack.is_empty():
            del self.stacks[index]
        return popped

if __name__ == '__main__':
    stacks = SetOfStacks(stack_size = 2)
    stacks.push(1)
    stacks.push(2)
    stacks.push(3)
    stacks.push(4)
    stacks.push(5)
    print(stacks)
    stacks.popAt(1)
    stacks.popAt(1)
    print(stacks)
    stacks.pop()
    print(stacks)