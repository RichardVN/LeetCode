"""
Topological Sort:

DataStructures:
    1. Adjacency Map of  Prerequisite Course :  [List of Associated Courses]
    2. Map of Course : In-Degree count
    3. Queue of courses with ZERO indegree  TODO: this means that we are now able to take the course

Procedure
- prepare the adjacency lists and indegree map structures.  Initialize queue with each course that has zero indegree, "no prereqs"
- While there are items in zero_indegree_queue:
    - pop course and add to res []
    - For each neighbor:  reduce in-degree by 1.
        - If in-degree is now 0, we can add neighbor to zero_indegree_queue

        
Time:  O( V + E )  ...  We pop each node from zero_indegree_queue  exactly once , giving us V.  For each Vertex we go over all neighbors, giving us E.
Space: O( V + E )  ...  zero_indegree_queue, can hold V courses. Adjacency lists of neighbors , holds E edges.
"""


from collections import defaultdict, deque
class Solution:

    def findOrder(self, numCourses, prerequisites):
        # Prepare the graph
        adj_list = defaultdict(list)

        # Map of Node : In-Degree
        indegree = {}
        for dest, src in prerequisites:
            adj_list[src].append(dest)

            # Record each node's in-degree
            indegree[dest] = indegree.get(dest, 0) + 1

        # Queue for maintaining list of nodes that have 0 in-degree
        zero_indegree_queue = deque([k for k in range(numCourses) if k not in indegree])

        topological_sorted_order = []

        # Until there are nodes in the Q
        while zero_indegree_queue:

            # Pop one node with 0 in-degree
            vertex = zero_indegree_queue.popleft()
            topological_sorted_order.append(vertex)

            # Reduce in-degree for all the neighbors
            if vertex in adj_list:
                for neighbor in adj_list[vertex]:
                    indegree[neighbor] -= 1

                    # Add neighbor to Q if in-degree becomes 0
                    if indegree[neighbor] == 0:
                        zero_indegree_queue.append(neighbor)

        # if len is not equal, that means we weren't able to take every course
        return topological_sorted_order if len(topological_sorted_order) == numCourses else []