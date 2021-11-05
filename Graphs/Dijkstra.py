from PriorityQueue import PriorityQueue
from Graph import Graph

def dijkstra(graph, start, end):
    visited = set()
    node_queue = PriorityQueue()
    node_queue_lookup = {}
    maximum_distance = 2 ** 31
    for node in graph.lookup:
        distance = maximum_distance
        if node == start:
            distance = 0
        node_queue_lookup[node] = node_queue.add(distance, node)
    path = []
    def get_node_cost(node):
        idx = node_queue_lookup[node]
        return node_queue.get_weight(idx)
    while not node_queue.is_empty():
        current = node_queue.peek()
        if current == end:
            break
        for neighbor in graph.get_neighbors(current):
            if neighbor in visited:
                continue
            current_node_cost = get_node_cost(current)
            node_distance = graph.get_distance(current, neighbor)
            new_distance = node_distance + current_node_cost
            existing_distance = get_node_cost(neighbor)
            if new_distance < existing_distance:
                neighbor_index = node_queue_lookup[neighbor]
                node_queue_lookup[neighbor] = node_queue.update_priority(neighbor_index, new_distance)
                path.append(current)
        node_queue.extract()
        visited.add(current)
        del node_queue_lookup[current]
    return path

if __name__ == '__main__':
    graph = Graph()
    for n in ['A', 'B', 'C', 'D']:
        graph.add(n)
    for e in [['A', 'B', 4], ['A', 'C', 3], ['B', 'D', 5], ['C', 'D', 7]]:
        graph.connect(e[0], e[1], distance = e[2])
    print(dijkstra(graph, 'A', 'D'))