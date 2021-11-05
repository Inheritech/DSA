from QueueLinkedList import Queue

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left_node = None
        self.right_node = None
    
    def __str__(self):
        return str(self.value)

    def set_left_child(self, child_node):
        self.left_node = child_node

    def set_right_child(self, child_node):
        self.right_node = child_node

    def add_node(self, child_node):
        """Add a the given node to the next available space in level order"""
        next = Queue()
        next.enqueue(self)
        while not next.is_empty():
            node = next.dequeue()
            if node.left_node is not None:
                next.enqueue(node.left_node)
            else:
                node.left_node = child_node
                return
            if node.right_node is not None:
                next.enqueue(node.right_node)
            else:
                node.right_node = child_node
                return

    def delete_node(self, value):
        """Remove the last node in the tree"""
        next = Queue()
        next.enqueue(self)
        to_delete = None
        last_parent = None
        while not next.is_empty():
            node = next.dequeue()
            last_node = node
            if node.value == value:
                to_delete = node
            if node.left_node or node.right_node:
                last_parent = node
            if node.left_node is not None:
                next.enqueue(node.left_node)
            if node.right_node is not None:
                next.enqueue(node.right_node)
        if to_delete is None:
            return
        last_node = last_parent.left_node if last_parent.right_node is None else last_parent.right_node
        to_delete.value = last_node.value
        if last_parent.right_node is None:
            last_parent.left_node = None
        else:
            last_parent.right_node = None
        


# Depth first search algorithms

def preorder_traversal(tree):
    yield tree
    if tree.left_node is not None:
        yield from preorder_traversal(tree.left_node)
    if tree.right_node is not None:
        yield from preorder_traversal(tree.right_node)

def inorder_traversal(tree):
    if tree.left_node is not None:
        yield from inorder_traversal(tree.left_node)
    yield tree
    if tree.right_node is not None:
        yield from inorder_traversal(tree.right_node)

def postorder_traversal(tree):
    if tree.left_node is not None:
        yield from postorder_traversal(tree.left_node)
    if tree.right_node is not None:
        yield from postorder_traversal(tree.right_node)
    yield tree

# Breadth first search algorithms

def levelorder_traversal(tree):
    next = Queue()
    next.enqueue(tree)
    while not next.is_empty():
        node = next.dequeue()
        if node.left_node is not None:
            next.enqueue(node.left_node)
        if node.right_node is not None:
            next.enqueue(node.right_node)
        yield node

# Node search algorithms

def find_node(tree, value):
    for node in levelorder_traversal(tree):
        if node.value == value:
            return node
    return None

# Tree printing algorithms

def print_tree(tree):
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
        left_len = len(left.split('\n')[0])
        right_len = len(right.split('\n')[0])
        total_width = max(left_len, right_len) * 2 + 1
        left_width = (total_width - 1) // 2
        right_width = total_width - 1 - left_width
        parent_str = create_divided_multistring(parent, total_width)
        connector_str = create_divided_string('┌', left_width, right_char = '─') + '┴' + create_divided_string('┐', right_width, left_char = '─')
        left_str_coll = left.split('\n')
        right_str_coll = right.split('\n')
        if len(left_str_coll) != len(right_str_coll):
            needed = abs(len(left_str_coll) - len(right_str_coll))
            if len(left_str_coll) > len(right_str_coll):
                right_str_coll.extend([' '] * needed)
            else:
                left_str_coll.extend([' '] * needed)
        children_coll = [create_divided_string(l, left_width) + ' ' + create_divided_string(r, right_width) for (l, r) in zip(left_str_coll, right_str_coll)]
        children_str = '\n'.join(children_coll)
        result = '\n'.join([parent_str, connector_str, children_str])
        return result
    def generate_placeholder(width, height = 3):
        return '\n'.join([' ' * width for i in range(height)])
    def generate(node):
        if not node.left_node and not node.right_node:
            return encapsulate(str(node))
        else:
            left_node = generate(node.left_node) if node.left_node else None
            right_node = generate(node.right_node) if node.right_node else None
            if left_node is None:
                left_node = generate_placeholder(len(right_node.split('\n')[0]))
            if right_node is None:
                right_node = generate_placeholder(len(left_node.split('\n')[0]))
            result = connect(encapsulate(str(node)), left_node, right_node)
            return result
    print(generate(tree))

if __name__ == '__main__':
    tree = TreeNode('N1')
    child_1 = TreeNode('N2')
    child_2 = TreeNode('N3')
    child_3 = TreeNode('N4')
    child_4 = TreeNode('N5')
    child_5 = TreeNode('N6')
    child_6 = TreeNode('N7')

    tree.set_left_child(child_1)

    child_1.set_left_child(child_3)
    child_1.set_right_child(child_4)

    tree.set_right_child(child_2)
    
    child_2.set_left_child(child_5)
    child_2.set_right_child(child_6)

    child_3.set_left_child(TreeNode('N8'))
    child_3.set_right_child(TreeNode('N9'))

    print("PreOrder traversal: ", " -> ".join([str(n) for n in preorder_traversal(tree)]))
    print("InOrder traversal: ", " -> ".join([str(n) for n in inorder_traversal(tree)]))
    print("PostOrder traversal: ", " -> ".join([str(n) for n in postorder_traversal(tree)]))
    print("LevelOrder traversal: ", " -> ".join([str(n) for n in levelorder_traversal(tree)]))
    print("Find N5 node: ", str(find_node(tree, 'N5')))

    print_tree(tree)
    tree.add_node(TreeNode('N10'))
    print_tree(tree)
    tree.delete_node('N3')
    print_tree(tree)