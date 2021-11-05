class TreeNode:
    def __init__(self, value):
        self.ancestor = None
        self.children = []
        self.value = value

    def __str__(self, level = 0):
        string = "  " * level + str(self.value) + "\n"
        for child in self.children:
            string += child.__str__(level + 1)
        return string

    def __iter__(self): # Might not want to treat this as a container
        return self.children

    def add_child(self, child_node):
        self.children.append(child_node)

if __name__ == '__main__':
    tree = TreeNode('Root')
    child_1 = TreeNode('Child 1')
    child_2 = TreeNode('Child 2')
    tree.add_child(child_1)
    tree.add_child(child_2)
    print(tree)