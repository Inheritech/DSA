from LinkedBinaryTree import print_tree
from CircularQueue import CircularQueue
from QueueLinkedList import Queue

class AVLTreeNode:
    def __init__(self, value):
        self.value = value
        self.left_node = None
        self.right_node = None

    def __str__(self):
        return str(self.value)
    
def balance_nodes(top, middle, bottom):
    def flip(left, right):
        left_value = left.value
        left.value = right.value
        right.value = left_value
    if top.left_node is middle:
        if middle.left_node is bottom: # Left Left
            top.right_node = middle
            middle.left_node = None
            top.left_node = bottom
            flip(top, middle)
        else: # Left Right
            middle.right_node = None
            top.right_node = bottom
            flip(top, bottom)
    else:
        if middle.right_node is bottom: # Right Right
            top.left_node = middle
            middle.right_node = None
            top.right_node = bottom
            flip(top, middle)
        else:
            middle.left_node = None
            top.left_node = bottom
            flip(top, bottom)

def add_node(root, value):
    parent_nodes = CircularQueue(2)
    search_node = root
    created_node = None
    while search_node:
        if search_node.value < value:
            if search_node.left_node is None:
                parent_nodes.enqueue(search_node)
            else:
                parent_nodes.clear()
            if search_node.right_node is None:
                created_node = AVLTreeNode(value)
                search_node.right_node = created_node
                break
            else:
                search_node = search_node.right_node
        else:
            if search_node.right_node is None:
                parent_nodes.enqueue(search_node)
            else:
                parent_nodes.clear()
            if search_node.left_node is None:
                created_node = AVLTreeNode(value)
                search_node.left_node = created_node
                break
            else:
                search_node = search_node.left_node

    if len(parent_nodes) == 2:
        top = parent_nodes.dequeue()
        middle = parent_nodes.dequeue()
        balance_nodes(top, middle, created_node)

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

# Node algorithms

def find_node(tree, value):
    current_node = tree
    while current_node:
        if current_node.value == value:
            return current_node
        elif current_node.value < value:
            current_node = current_node.right_node
        else:
            current_node = current_node.left_node
    return current_node

def delete_node(tree, value):
    parent_node = None
    search_node = tree
    while search_node:
        if search_node.value == value:
            break
        elif search_node.value < value:
            parent_node = search_node
            search_node = search_node.right_node
        else:
            parent_node = search_node
            search_node = search_node.left_node

    if not search_node:
        return

    target_node = search_node

    def delete(parent_node, target_node):
        if not target_node.left_node and not target_node.right_node:
            if not parent_node:
                return
            if parent_node.left_node is target_node:
                parent_node.left_node = None
            else:
                parent_node.right_node = None
        elif target_node.left_node and target_node.right_node:
            successor = target_node.right_node
            successor_parent = target_node
            while successor.left_node:
                successor_parent = successor
                successor = successor.left_node
            target_node.value = successor.value
            delete(successor_parent, successor)    
        else:
            successor = target_node.left_node if target_node.left_node else target_node.right_node
            target_node.value = successor.value
            delete(target_node, successor)

    delete(parent_node, target_node)
    
    # Balance
    top = parent_node
    if all([top.left_node, top.right_node]) or not any([top.left_node, top.right_node]):
        return
    
    middle = top.left_node if top.left_node else top.right_node
    if all([middle.left_node, middle.right_node]) or not any([middle.left_node, middle.right_node]):
        return
    
    bottom = middle.left_node if middle.left_node else middle.right_node
    balance_nodes(top, middle, bottom) 

        

if __name__ == '__main__': 
    tree = AVLTreeNode(70)
    to_add = [50, 90, 30, 60, 80, 100, 20, 110, 65, 75]
    for n in to_add:
        add_node(tree, n)
    print_tree(tree)
    print("PreOrder traversal: ", " -> ".join([str(n) for n in preorder_traversal(tree)]))
    print("InOrder traversal: ", " -> ".join([str(n) for n in inorder_traversal(tree)]))
    print("PostOrder traversal: ", " -> ".join([str(n) for n in postorder_traversal(tree)]))
    print("LevelOrder traversal: ", " -> ".join([str(n) for n in levelorder_traversal(tree)]))
    print("Find 60 node: ", str(find_node(tree, 60)))
    add_node(tree, 10)
    print_tree(tree)
    add_node(tree, 120)
    print_tree(tree)
    add_node(tree, 62)
    print_tree(tree)
    add_node(tree, 78)
    print_tree(tree)

    tree = AVLTreeNode(80)
    for n in [50, 90, 30, 60, 80, 100, 20, 40, 70, 110, 15]:
        add_node(tree, n)
    print_tree(tree)
    delete_node(tree, 40)
    print_tree(tree)