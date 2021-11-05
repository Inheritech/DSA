class Heap:
    def __init__(self, min = True):
        self.list = [None]
        if min:
            self.comparer = lambda parent, node: parent < node
        else:
            self.comparer = lambda parent, node: parent > node

    def peek(self):
        return self.list[1]

    def __len__(self):
        return len(self.list) - 1

    def get_node(self, index):
        if index >= len(self.list):
            return None
        return self.list[index]

    def __limit_index(self, index):
        if index >= len(self.list) or index < 1:
            return None
        return index

    def get_left_child_location_of(self, index):
        return self.__limit_index(index * 2)


    def get_right_child_location_of(self, index):
        return self.__limit_index(index * 2 + 1)

    def get_parent_location_of(self, index):
        return self.__limit_index(index // 2)

    def __flip_nodes(self, left, right):
        left_value = self.list[left]
        self.list[left] = self.list[right]
        self.list[right] = left_value

    def heapify_up(self, index):
        current = index
        parent = self.get_parent_location_of(current)
        while parent:
            if not self.comparer(self.get_node(parent), self.get_node(current)):
                self.__flip_nodes(parent, current)
                current = parent
                parent = self.get_parent_location_of(current)
            else:
                break
        return current

    def heapify_down(self, index = 1):
        current = index
        def test_nodes(parent, child):
            return child if not self.comparer(self.get_node(parent), self.get_node(child)) else None
        while current:
            flip_child = None
            left_child = self.get_left_child_location_of(current)
            right_child = self.get_right_child_location_of(current)
            if left_child and right_child:
                flip_child = left_child if self.get_node(left_child) < self.get_node(right_child) else right_child
            elif any([left_child, right_child]):
                flip_child = left_child
                
            if flip_child:
                flip_child = test_nodes(current, flip_child)
            
            if not flip_child:
                break

            self.__flip_nodes(current, flip_child)
            current = flip_child
        return current
            

    def add(self, value):
        self.list.append(value)
        new_index = len(self)
        return self.heapify_up(new_index)

    def extract(self):
        value = self.list[1]
        self.list[1] = self.list.pop()
        self.heapify_down()
        return value

    def update(self, index, new_value):
        current_value = self.get_node(index)
        if current_value is None or current_value == new_value:
            return index
        self.list[index] = new_value
        if self.comparer(current_value, new_value):
            return self.heapify_down(index)
        else:
            return self.heapify_up(index)


# Tree printing algorithms

def print_tree(tree, node = 1):
    def encapsulate(text):
        text_len = len(text)
        return "┌─" + ("─") * text_len + "─┐\n" + "│ " + text + " │\n" + "└─" + ("─") * text_len + "─┘"
    def create_divided_multistring(middle, size, left_char = ' ', right_char = ' '):
        return '\n'.join([create_divided_string(s, size) for s in middle.split('\n')])
    def create_divided_string(middle, size, left_char = ' ', right_char = ' '):
        left_len = int((size - len(middle)) // 2)
        right_len = int(size - len(middle) - left_len)
        return (left_char * left_len) + middle + (right_char * right_len)
    def connect(parent, left, right):
        total_width = (max(len(left.split('\n')[0]),len(right.split('\n')[0])) * 2) + 1
        left_width = (total_width - 1) // 2
        right_width = total_width - 1 - left_width
        parent_str = create_divided_multistring(parent, total_width)
        left_adjusted = create_divided_multistring(left, left_width)
        right_adjusted = create_divided_multistring(right, right_width)
        connector_str = create_divided_string('┌', left_width, right_char = '─') + '┴' + create_divided_string('┐', right_width, left_char = '─')
        left_str_coll = left_adjusted.split('\n')
        right_str_coll = right_adjusted.split('\n')
        children_coll = [l + ' ' + r for (l, r) in zip(left_str_coll, right_str_coll)]
        if len(left_str_coll) != len(right_str_coll):
            larger = left if len(left_str_coll) > len(right_str_coll) else right
            shorter = right if larger is left else left
            children_coll.extend(larger.split('\n')[-(len(larger.split('\n')) - len(shorter.split('\n'))):])
        children_str = '\n'.join(children_coll)
        result = '\n'.join([parent_str, connector_str, children_str])
        return result
    def generate_placeholder(width, height = 3):
        return '\n'.join([' ' * width for i in range(height)])
    def generate(tree, node = 1):
        left_node = tree.get_left_child_location_of(node)
        right_node = tree.get_right_child_location_of(node)
        if not left_node and not right_node:
            return encapsulate(str(tree.get_node(node)))
        else:
            left_node_str = None
            right_node_str = None
            if left_node:
                left_node_str = generate(tree, left_node)
            if right_node:
                right_node_str = generate(tree, right_node)
            if left_node_str is None:
                left_node_str = generate_placeholder(len(right_node_str.split('\n')[0]))
            if right_node_str is None:
                right_node_str = generate_placeholder(len(left_node_str.split('\n')[0]))
            result = connect(encapsulate(str(tree.get_node(node))), left_node_str, right_node_str)
            return result
    print(generate(tree))

if __name__ == '__main__':
    heap = Heap()
    for n in [10, 20, 30, 40, 9, 6, 8, 50]:
        heap.add(n)
    print_tree(heap)
    heap.add(5)
    print_tree(heap)
    heap.extract()
    print_tree(heap)
    heap.extract()
    print_tree(heap)
    heap.extract()
    print_tree(heap)