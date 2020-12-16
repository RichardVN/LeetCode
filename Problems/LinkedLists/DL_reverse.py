def reverse(head):
    temp = None

    current = head

    while current:
        temp = current.prev
        current.prev = current.next
        current.next = temp
        temp = current
        current = current.prev
    
    # head should now be at temp.prev if it is not None (single element list)
    head = temp.prev
    return head