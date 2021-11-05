from LinkedList import LinkedList, generate_linked_list

def partition(l, n):
    node = l.head
    tail = l.head
    while node:
        current_node = node
        node = node.next
        current_node.next = None
        if current_node.value < n:
            if current_node == l.head:
                continue
            current_node.next = l.head
            l.head = current_node
        else:
            tail.next = current_node
            tail = current_node
    return l

if __name__ == '__main__':
    l = generate_linked_list(10, 0, 99)
    print(l)
    print(partition(l, 50))