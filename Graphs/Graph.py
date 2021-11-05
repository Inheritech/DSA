from QueueLinkedList import Queue
from StackLinkedList import Stack

class Graph:
    def __init__(self):
        self.lookup = {}
        self.distances = {}

    def add(self, value):
        self.lookup[value] = []

    def connect(self, source, target, bidirectional = True, distance = 1):
        if not target in self.lookup[source]:
            self.lookup[source].append(target)
            self.distances[(source, target)] = distance

        if bidirectional:
            if not source in self.lookup[target]:
                self.lookup[target].append(source)
                self.distances[(target, source)] = distance

    def get_distance(self, source, target):
        return self.distances[(source, target)]

    def get_neighbors(self, of):
        if of in self.lookup:
            return self.lookup[of]

def breadth_first_search(graph, start):
    visited = set()
    pending = Queue()
    visited.add(start)
    pending.enqueue(start)
    while not pending.is_empty():
        current = pending.dequeue()
        neighbors = graph.get_neighbors(current)
        for neighbor in neighbors:
            if neighbor not in visited:
                pending.enqueue(neighbor)
                visited.add(neighbor)
        yield current

def depth_first_search(graph, start):
    visited = set()
    pending = Stack()
    visited.add(start)
    pending.push(start)
    while not pending.is_empty():
        current = pending.pop()
        neighbors = graph.get_neighbors(current)
        for neighbor in neighbors:
            if neighbor not in visited:
                pending.push(neighbor)
                visited.add(neighbor)
        yield current

def topological_sort(graph, start = None):
    visited = set()
    result = Stack()
    def visit(node):
        neighbors = graph.get_neighbors(node)
        for n in neighbors:
            if n not in visited:
                visit(n)
        result.push(node)
        visited.add(node)
    if start:
        visit(start)
    else:
        for k in graph.lookup:
            if k not in visited:
                visit(k)
    result_list = []
    while not result.is_empty():
        result_list.append(result.pop())
    return result_list

def bfs_source_shortest_path(graph, start, end):
    pending = Queue()
    visited = set()
    pending.enqueue(start)
    parents = {}
    while not pending.is_empty():
        node = pending.dequeue()
        if node not in visited:
            visited.add(node)
            for n in graph.get_neighbors(node):
                if n not in visited:
                    parents[n] = node
                    pending.enqueue(n)
    path = []
    backtrack_node = end
    while backtrack_node:
        path.append(backtrack_node)
        if backtrack_node in parents:
            backtrack_node = parents[backtrack_node]
        else:
            break
    path.reverse()
    return path            

if __name__ == '__main__':
    graph = Graph()
    graph.add('A')
    graph.add('B')
    graph.add('C')
    graph.add('D')
    graph.add('E')
    graph.add('F')
    graph.add('G')
    graph.connect('A', 'B')
    graph.connect('A', 'C')
    graph.connect('B', 'D')
    graph.connect('B', 'G')
    graph.connect('C', 'D')
    graph.connect('C', 'E')
    graph.connect('D', 'F')
    graph.connect('E', 'F')
    graph.connect('F', 'G')
    print(graph.lookup)
    print(" -> ".join([n for n in breadth_first_search(graph, 'A')]))
    print(" -> ".join([n for n in depth_first_search(graph, 'A')]))
    print("Shortest path from A to G: ")
    print(" -> ".join([n for n in bfs_source_shortest_path(graph, 'A', 'G')]))

    graph = Graph()
    for n in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
        graph.add(n)
    for e in [['A', 'C'], ['B', 'C'], ['B', 'D'], ['C', 'E'], ['D', 'F'], ['E', 'H'], ['F', 'G'], ['E', 'F']]:
        graph.connect(e[0], e[1], bidirectional = False)
    
    print(topological_sort(graph))