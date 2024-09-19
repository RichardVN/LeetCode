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
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # adj lists of prereq to course
        neighbors = defaultdict(list)
        indegrees = defaultdict(int)
        
        zero_indegree = deque()
        res = []
        
        # populating neighbor adjacency lists, indegree map, and zero_degree queue
        for course, prereq in prerequisites:
            neighbors[prereq].append(course)
            indegrees[course] += 1
        
        #TODO: make sure to go thru all courses, not just courses with neighbors
        for course in range(0, numCourses):
            if course not in indegrees.keys():
                zero_indegree.append(course)

        # while we can take a course with no prereq
        while zero_indegree:
            takenCourse = zero_indegree.popleft()
            res.append(takenCourse)
            # we fulfilled this prereq
            for neighbor in neighbors[takenCourse]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    zero_indegree.append(neighbor)

        #TODO: if cant take all courses, return empty list
        return res if len(res) == numCourses else []
        
