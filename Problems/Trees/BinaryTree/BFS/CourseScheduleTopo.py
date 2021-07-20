"""
https://leetcode.com/problems/course-schedule/discuss/368508/Python3-Breadth-first-search-for-cycle-detection
https://courses.cs.washington.edu/courses/cse326/03wi/lectures/RaoLect20.pdf

Topological Sort Approach BFS: 
    - Each course is a Node
    - A -> B  means A is a Prerequisite for B, A has no prereq
    - NOTE: find a linear ordering of classes such that all arrows point right
    
Procedure:
    - Create adjacency dictionary  {Course : Set of Neighbors}
    - Create In-Degree dictionary  {Course : Prerequisites_left}
    - Initialize queue with all classes that have no prerequisites left
    - While q:
        - pop class "aka take the course"
        - For every neighbor of the course we just completed, we can reduce prereq by 1
            - if no more prereq, we can push onto queue
    - If no more q (no more classes we can take), but still course with indegree, FALSE
    
    
TIME: O( V + E ) for bfs traversal .... O(E)  to build graph  O(V) to build indegree map  
SPACE:  O(V + E), V keys, E edges in set  ... O(V) to build prereq_required map
"""
from collections import defaultdict
from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. Initialize Indegree array O(|V|)   and   adjacency list  O(|E|)
        # NOTE. must have indegree for each course / vertex
        prereq_required = {course : 0 for course in range(numCourses)}
        graph = defaultdict(set)
        
        for course, prereq in prerequisites:
            # add course to neighbor set
            graph[prereq].add(course)
            # update indegree of course
            prereq_required[course] += 1
        
        # Initialize Queue.   O(|V|)
        q = deque()
        for course, prereq_left in prereq_required.items():
            if prereq_left == 0:
                q.append(course)
                
        #  Visit each vertex and its edges worst case O(|V| + |E|)
        # while q, aka while there are classes i can take
        while q:
            # "take" the course
            course = q.popleft()
            
            # remove course from indegree dictionary
            prereq_required.pop(course)
            
            # Course is a prereq for all neighbors. Find neighbors and reduce prereq by 1
            neighbor_set = graph[course]
            
            
            for neighbor in neighbor_set:
                prereq_required[neighbor] -= 1
                # If course has no prereq, we can take the course. Append to queue
                if prereq_required[neighbor] == 0:
                    q.append(neighbor)
                    
        # q ends. no possible classes left. If anything left in prereq, means we cant take course
        return not prereq_required
        