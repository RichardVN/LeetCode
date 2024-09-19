"""
TODO: Djikstra's is identical to iterative BFS ... except for our datastructure we use a MIN heap of tuples:  (distance_from_source, Node)

To see if we visited all nodes, check Visited set with number of nodes

TIME: O(V  +  E * log V)  ...  push/pop on heap of size V costs log V.  We do this for E edges.
SPACE: O(E + V) ...  Edges and Heap of V vertices
"""

from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:        
        destination = n
        start = k
        adj_list = defaultdict(list)
        
        for a, b, time in times:
            adj_list[a].append((time, b))
        
        visited=set()
        heap = [(0, start)]
        while heap:
            # we take the node with MINIMUM time to get to
            sourceToNodeTime, node = heapq.heappop(heap)    # log V
            print(f'{sourceToNodeTime=} {node=}')

            # mark node as visited so we dont have to revisit
            visited.add(node)
            
            # TODO: we have hit ALL nodes ... 'all nodes have received signal'
            if len(visited)==n:
                return sourceToNodeTime
            
            for nodeToNeighborTime, neighbor_node in adj_list[node]:
                if neighbor_node not in visited:
                    heapq.heappush(heap, (sourceToNodeTime + nodeToNeighborTime, neighbor_node))
                
        return -1