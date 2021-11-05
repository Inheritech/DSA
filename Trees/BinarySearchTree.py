from LinkedBinaryTree import print_tree
from QueueLinkedList import Queue

class BinarySearchTreeNode:
    def __init__(self, value):
        self.value = value
        self.left_node = None
        self.right_node = None

    def __str__(self):
        return str(self.value)
    
def add_node(root, value):
    current_node = root
    if current_node.value < value:
        if current_node.right_node is None:
            current_node.right_node = BinarySearchTreeNode(value)
        else:
            add_node(current_node.right_node, value)
    else:
        if current_node.left_node is None:
            current_node.left_node = BinarySearchTreeNode(value)
        else:
            add_node(current_node.left_node, value)

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
            successor_parent = None
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

        

if __name__ == '__main__':
    tree = BinarySearchTreeNode(50)
    print_tree(tree)
    add_node(tree, 25)
    add_node(tree, 75)
    print_tree(tree)
    add_node(tree, 60)
    print_tree(tree)
    delete_node(tree, 50)
    print_tree(tree)
    print("PreOrder traversal: ", " -> ".join([str(n) for n in preorder_traversal(tree)]))
    print("InOrder traversal: ", " -> ".join([str(n) for n in inorder_traversal(tree)]))
    print("PostOrder traversal: ", " -> ".join([str(n) for n in postorder_traversal(tree)]))
    print("LevelOrder traversal: ", " -> ".join([str(n) for n in levelorder_traversal(tree)]))
    print("Find 60 node: ", str(find_node(tree, 60)))