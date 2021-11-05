class PriorityQueue:
    def __init__(self, min = True):
        self.weights = [None]
        self.items = [None]
        self.comparator = lambda left, right: left < right if min else lambda left, right: left > right

    def __len__(self):
        return len(self.weights) - 1

    def __limit_index(self, index):
        if index is None:
            return None
        if index < 1 or index >= len(self.weights):
            return None
        return index

    def __swap_indexes(self, left, right):
        left_weight = self.weights[left]
        self.weights[left] = self.weights[right]
        self.weights[right] = left_weight
        left_item = self.items[left]
        self.items[left] = self.items[right]
        self.items[right] = left_item

    def __compare_indexes(self, left, right):
        return self.comparator(self.get_weight(left), self.get_weight(right))

    def __get_smallest_weight(self, left, right):
        if not left and not right:
            return None
        left = self.__limit_index(left)
        right = self.__limit_index(right)
        if left:
            if right:
                return left if self.get_weight(left) < self.get_weight(right) else right
            else:
                return left
        else:
            return None

    def __heapify_up(self, index):
        if not self.__limit_index(index):
            return
        current = index
        while current:
            parent_idx = self.get_parent_location_of(current)
            if parent_idx is None:
                break
            if self.__compare_indexes(parent_idx, current):
                break
            self.__swap_indexes(parent_idx, current)
            current = parent_idx
        return current

    def __heapify_down(self, index = 1):
        if not self.__limit_index(index):
            return
        current = index
        while current:
            flip_child = self.__get_smallest_weight(self.get_left_child_of(current), self.get_right_child_of(current))
            if not flip_child:
                break
            if self.get_weight(flip_child) >= self.get_weight(current):
                break
            self.__swap_indexes(flip_child, current)
            current = flip_child
        return current

    def get_parent_location_of(self, index):
        location = index // 2
        return self.__limit_index(location)

    def get_left_child_of(self, index):
        location = index * 2
        return self.__limit_index(location)

    def get_right_child_of(self, index):
        location = index * 2 + 1
        return self.__limit_index(location)

    def get_weight(self, index):
        if not self.__limit_index(index):
            return None
        return self.weights[index]

    def get_item(self, index):
        if not self.__limit_index(index):
            return None
        return self.items[index]
    
    def add(self, priority, value):
        self.weights.append(priority)
        self.items.append(value)
        new_index = len(self.weights) - 1
        return self.__heapify_up(new_index)

    def peek(self):
        return self.items[1]

    def is_empty(self):
        return len(self) == 0

    def extract(self):
        value = self.items[1]
        self.weights[1] = self.weights[-1]
        self.items[1] = self.items[-1]
        self.weights.pop()
        self.items.pop()
        self.__heapify_down()
        return value

    def update_priority(self, index, new_priority):
        if not self.__limit_index(index):
            return None
        previous_priority = self.weights[index]
        self.weights[index] = new_priority
        if self.comparator(new_priority, previous_priority):
            return self.__heapify_up(index)
        else:
            return self.__heapify_down(index)

if __name__ == '__main__':
    queue = PriorityQueue()
    queue.add(10, 10)
    queue.add(20, 20)
    queue.add(15, 15)
    idx = queue.add(25, 25)
    queue.add(30, 30)
    queue.update_priority(idx, 35)
    while not queue.is_empty():
        print(queue.extract())