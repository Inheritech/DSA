from LinkedList import LinkedList, generate_linked_list

def sum_linked_lists(left, right):
    left_pointer = left.head
    right_pointer = right.head

    result = LinkedList()
    remainder = 0
    while left_pointer and right_pointer:
        node_sum = left_pointer.value + right_pointer.value
        result.add((node_sum % 10) + remainder)
        remainder = node_sum // 10
        left_pointer = left_pointer.next
        right_pointer = right_pointer.next
    
    remaining_digits = None

    if left_pointer is not None:
        remaining_digits = left_pointer
    if right_pointer is not None:
        remaining_digits = right_pointer
    
    if remaining_digits is not None:
        result.add(remaining_digits.value + remainder)
        remaining_digits = remaining_digits.next
        while remaining_digits:
            result.add(remaining_digits.value)
            remaining_digits = remaining_digits.next
    elif remainder != 0:
        result.add(remainder)

    return result

if __name__ == '__main__':
    left = generate_linked_list(5, 0, 9)
    right = generate_linked_list(6, 0, 9)
    print(left)
    print(" + ")
    print(right)
    print(sum_linked_lists(left, right))