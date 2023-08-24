"""
COPY question => hashmap of old to copy

RECURSIVE BUILD => dfs(node)-> Node helper
    Base Case:
    -> return copyNode from map  (in the case of Trees we would have a base case return None to stop dfs)


    Recursive case:
    1. allocate New copyNode = Node(..)
    2. recursively build out children/neighbors of copyNode
    3. return copyNode

Time: O(E + V), edges and vertices
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # returns the COPYNODE
        # allocates new copyNode, recursively build out is neighbors, returns copyNode
        def dfs(node):
            if not node: return None

            # already clone
            if node in oldToCopy:
                return oldToCopy[node]
            
            copyNode = Node(node.val)
            oldToCopy[node] = copyNode # TODO: do this before recursive calls. or else it will trivially cycle back

            for n in node.neighbors:
                copyNode.neighbors.append(dfs(n))

            return copyNode

        oldToCopy = {}
        return dfs(node)