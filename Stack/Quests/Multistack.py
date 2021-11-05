# Use a single list to implement three stacks

class Multistack:
    def __init__(self, stack_size):
        self.stack_amount = 3
        self.stack_size = stack_size
        self.list = [None] * (self.stack_amount * self.stack_size)
        self.sizes = [0] * self.stack_size

    def is_full(self, stack):
        return self.sizes[stack] == self.stack_size

    def is_empty(self, stack):
        return self.sizes[stack] == 0

    def __stack_offset(self, stack):
        return self.stack_size * stack

    def push(self, stack, value):
        if self.is_full(stack):
            return # Should raise error or bool
        else:
            self.list[self.__stack_offset(stack) + self.sizes[stack]] = value
            self.sizes[stack] += 1
        
    def pop(self, stack):
        if self.is_empty(stack):
            return None
        else:
            value =  self.list[self.__stack_offset(stack) + self.sizes[stack] - 1]
            self.list[self.__stack_offset(stack) + self.sizes[stack] - 1] = None
            self.sizes[stack] -= 1
            return value

    def clear(self, stack):
        stack_offset = self.__stack_offset(stack)
        self.list[stack_offset:stack_offset + self.stack_size] = [None] * self.stack_size
        self.sizes[stack] = 0

    def get_stack(self, stack):
        stack_offset = self.__stack_offset(stack)
        return [x for x in self.list[stack_offset:stack_offset + self.stack_size] if x is not None]

if __name__ == '__main__':
    stack = Multistack(3)
    stack.push(0, 4)
    stack.push(0, 5)
    stack.push(0, 3)
    stack.push(1, 1)
    stack.push(1, 2)
    print(stack.get_stack(0))
    print(stack.get_stack(1))
    print(stack.pop(0))
    print(stack.get_stack(0))
    print(stack.clear(1))
    print(stack.get_stack(1))