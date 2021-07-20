"""
Intuition: 
    1. Serialize Function
        - Global array for data to append values
        - Utilize recursive helper function:  rtype VOID
            - Base:  Hit None node -> append "N"
            - Recursive: Hit value Node -> append current.val, recursive call children
    2. Deserialize:
        - We have a global data array that we step thru once per value with global pointer
        - Utilize recursive helper:  rtype TREENODE
            - Base:  Hit "N" value. -> Return None, jump ptr
            - Recursive: Value -> Create TreeNode(Value), jump ptr, recursive call to return left and right children nodes
                - Return Current node upwards
"""

class Codec:

    def serialize(self, root):
        # Recursive helper function. Modifies array, returns Void
        def dfs(current):
            # base case. None node, we append N
            if not current:
                node_vals.append("N")
                # base case needs a return so we dont drop into recursive
                return
            # Recursive Case. There is a value node, append value. Then recursively call children.
            # 1. Process node by appending. Append STRING type for join later
            node_vals.append(str(current.val))
            # 2. Recursive calls on children to append their values
            dfs(current.left)
            dfs(current.right)
            # 3. Nothing to return, already modified array.
        
        # MAIN shell function
        if not root:
            return ""
        # array of str numbers
        node_vals = []
        dfs(root)
        # join together array of numbers
        return ",".join(node_vals)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # global pointer of where we are in reading data array
        self.i = 0
        
        """ Recursive function that reads data from pointer, returns a Node """
        def recurse(data):
            # base case: We hit "N" character and have to return a None node
            if data[self.i] == "N":
                self.i += 1
                return None
            # Recursive Case. We have not hit none, we have to recurse deeper left and right again
            # 1. Process current node, create tree node, increment i
            value = int(data[self.i])
            self.i += 1
            node  = TreeNode(value)
            # 2. Recursively build left and right children
            node.left = recurse(data)
            node.right = recurse(data)  
            # 3. Return Node (same type as base case) up the tree
            return node

        # MAIN shell function
        if not data:
            return None
        # convert data to list of ints
        data = data.split(",")
        # return the recursively built root
        root = recurse(data)
        return root
        



"""
BFS Iterative Version
- Only append a node after we pop it and make sure its not None
    - Then we append Children to queue
"""
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        q, res = collections.deque([root]), []
        while q:
            node = q.popleft()
            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append('#')
                
        return ' '.join(res)    

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data[0] == '#':
            return
        vals = iter(data.split())
        root = TreeNode(int(next(vals)))
        q = collections.deque([root])
        while q:
            q_len = len(q)
            for _ in range(q_len):
                node = q.popleft()
                l, r = next(vals), next(vals)
                node.left = None if l == '#' else TreeNode(int(l))
                if node.left:
                    q.append(node.left)
                node.right = None if r == '#' else TreeNode(int(r))
                if node.right:
                    q.append(node.right)
        return root