from LinkedList import LinkedList, generate_linked_list

def nth_to_last(l, n):
    sequence_pointer = l.head
    offset_pointer = l.head

    for i in range(n):
        if offset_pointer is None:
            return None
        offset_pointer = offset_pointer.next
    
    while offset_pointer:
        sequence_pointer = sequence_pointer.next
        offset_pointer = offset_pointer.next
    return sequence_pointer

def get_node_sequence(node):
    while node:
        yield str(node)
        node = node.next

def print_node_sequence(node):
    print(" -> ".join(get_node_sequence(node)))

if __name__ == '__main__':
    l = generate_linked_list(10, 0, 99)
    print(l)
    print("Last 3: ")
    print_node_sequence(nth_to_last(l, 3))