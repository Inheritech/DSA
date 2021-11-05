from LinkedList import LinkedList, Node, generate_linked_list

def intersect(left, right):
    if left.tail is not right.tail:
        return None
    
    left_len = len(left)
    right_len = len(right)

    shorter = left if left_len < right_len else right
    longer = right if shorter is left else left

    len_difference = abs(left_len - right_len)
    longer_pointer = longer.head
    shorter_pointer = shorter.head

    for i in range(len_difference):
        longer_pointer = longer_pointer.next

    while longer_pointer is not shorter_pointer:
        longer_pointer = longer_pointer.next
        shorter_pointer = shorter_pointer.next

    return longer_pointer


if __name__ == '__main__':
    left = generate_linked_list(4, 0, 9)
    right = generate_linked_list(4, 0, 9)

    assert intersect(left, right) is None # Should be None

    conflicting = Node(7)

    left.tail.next = conflicting
    left.tail = conflicting
    right.tail.next = conflicting
    right.tail = conflicting

    print(intersect(left, right)) # Should be '7'

    left = generate_linked_list(6, 0, 9)
    right = generate_linked_list(3, 0, 9)

    assert intersect(left, right) is None # Should be None

    conflicting = Node(9)

    left.tail.next = conflicting
    left.tail = conflicting
    right.tail.next = conflicting
    right.tail = conflicting

    print(intersect(left, right)) # Should be '9'