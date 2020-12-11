class Node(object):

    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1

        if self.head is None:
            return -1

        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        # index outside linked list "indices"
        if index < 0 or index > self.size:
            return
        node = Node(val)
        # adding to head, we must change head pointer
        if index == 0:
            node.next = self.head
            self.head = node
        # adding to body or appending to tail. Iterate to index - 1 Node, and append after
        else:
            curr = self.head
            for i in range(index - 1):
                curr = curr.next
            node.next = curr.next
            curr.next = node
        self.size += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        # index invalid
        if index < 0 or index >= self.size:
            return

        curr = self.head
        # delete head. We must shift self.head
        if index == 0:
            self.head = curr.next
        else:
            for i in range(index - 1):
                curr = curr.next
            # set i-1 node point to i+1 node
            curr.next = curr.next.next

        self.size -= 1

    def printList(self):
        if self.head:
            current = self.head
            while current:
                print(current.val, end=' ')
                current = current.next
        else:
            print("Linked list is empty")

# Testing
my_linked_list = LinkedList()
my_linked_list.addAtHead(5)
my_linked_list.addAtHead(6)
my_linked_list.addAtTail(9)
my_linked_list.addAtIndex(0, 10)
my_linked_list.deleteAtIndex(2)

my_linked_list.printList()
