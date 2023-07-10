"""
Hash Map :  allows us to key -> Value  in O(1)
LinkedList:  allows us to eject from least_recently_used and add to most_recently_used in O(1)

TODO: 
    - create a Node class that has BOTH key and value attributes
    - main LRUCache class contains head, tail, and cache{}
    - add helper methods for removeNode(node) and addNodeTail(node)

- no need for self.size since we can just len(cache)
"""

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(-1, -1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head

        self.cache = {}
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key not in self.cache: return -1

        node = self.cache[key]
        self.removeNode(node)
        self.addTail(node)

        return node.val
        

    def put(self, key: int, value: int) -> None:
        # not in cache. Create new node and add to tail. Add node to cache
        if key not in self.cache:
            newNode = Node(key, value)
            self.addTail(newNode)
            self.cache[key] = newNode
        # in cache. Update node's value. shift node to tail.
        else:
            node = self.cache[key]
            node.val = value
            self.removeNode(node)
            self.addTail(node)
        # capacity?
        if len(self.cache.keys()) > self.capacity:
            # remove node
            node = self.head.next
            self.removeNode(node)
            # remove from cache
            del self.cache[node.key]
    
    def removeNode(self, node):
        before, after = node.prev, node.next
        before.next = after
        after.prev = before
    
    def addTail(self, node):
        after = self.tail
        before = self.tail.prev
        before.next = after.prev = node
        node.prev, node.next = before, after



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)