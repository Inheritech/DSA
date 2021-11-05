class BinaryTree:
    def __init__(self):
        self.list = [None]

    def __len__(self):
        return len(self.list) - 1

    def get_node(self, index):
        if index >= len(self.list):
            return None
        return self.list[index]
    
    def get_left_child_location_of(self, index):
        location = index * 2
        if location >= len(self.list):
            return None
        return location

    def get_right_child_location_of(self, index):
        location = index * 2 + 1
        if location >= len(self.list):
            return None
        return location

    def get_left_child_of(self, index):
        left_child_location = self.get_left_child_location_of(index)
        if left_child_location is None:
            return None
        return self.list[left_child_location]

    def get_right_child_of(self, index):
        right_child_location = self.get_right_child_location_of(index)
        if right_child_location is None:
            return None
        return self.list[right_child_location]

    def add(self, value):
        self.list.append(value)
        return len(self.list) - 1

    def delete(self, value):
        to_delete = None
        for i in range(1, len(self.list)):
            if self.list[i] == value:
                to_delete = i
                break
        last_value = self.list.pop()
        self.list[to_delete] = last_value

    def search(self, value):
        for i in range(1, len(self.list)):
            if self.list[i] == value:
                return i
        return None
    
# Depth first search algorithms

def preorder_traversal(tree, node = 1):
    yield tree.get_node(node)
    left_node = tree.get_left_child_location_of(node)
    right_node = tree.get_right_child_location_of(node)
    if left_node is not None:
        yield from preorder_traversal(tree, left_node)
    if right_node is not None:
        yield from preorder_traversal(tree, right_node)

def inorder_traversal(tree, node = 1):
    left_node = tree.get_left_child_location_of(node)
    right_node = tree.get_right_child_location_of(node)
    if left_node is not None:
        yield from inorder_traversal(tree, left_node)
    yield tree.get_node(node)
    if right_node is not None:
        yield from inorder_traversal(tree, right_node)

def postorder_traversal(tree, node = 1):
    left_node = tree.get_left_child_location_of(node)
    right_node = tree.get_right_child_location_of(node)
    if left_node is not None:
        yield from postorder_traversal(tree, left_node)
    if right_node is not None:
        yield from postorder_traversal(tree, right_node)
    yield tree.get_node(node)

# Breadth first search algorithms

def levelorder_traversal(tree):
    for i in range(1, len(tree) + 1):
        yield tree.get_node(i)

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
    tree = BinaryTree()
    for i in range(9):
        tree.add('N' + str(i + 1))

    print("PreOrder traversal: ", " -> ".join([str(n) for n in preorder_traversal(tree)]))
    print("InOrder traversal: ", " -> ".join([str(n) for n in inorder_traversal(tree)]))
    print("PostOrder traversal: ", " -> ".join([str(n) for n in postorder_traversal(tree)]))
    print("LevelOrder traversal: ", " -> ".join([str(n) for n in levelorder_traversal(tree)]))
    print("Find N5 node: ", str(tree.search('N5')))

    print_tree(tree)
    tree.add('N10')
    print_tree(tree)
    tree.delete('N3')
    print_tree(tree)