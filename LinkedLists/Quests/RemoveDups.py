from LinkedList import LinkedList, generate_linked_list

def remove_duplicates(l):
    existing_values = set()
    previous_node = None
    for node in l:
        if node.value in existing_values:
            previous_node.next = node.next
            del node
        else:
            existing_values.add(node.value)
            previous_node = node
    return l

if __name__ == '__main__':
    l = generate_linked_list(10, 0, 50)
    print(l)
    print(remove_duplicates(l))