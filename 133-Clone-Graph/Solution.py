"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        from collections import deque

        if not node:
            return None

        nodesDictionary = {}
        nodesDictionary[node] = Node(node.val)
        queue = deque([node])

        while queue:
            currentNode = queue.popleft()
            for neighbor in currentNode.neighbors:
                if neighbor not in nodesDictionary:
                    nodesDictionary[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                nodesDictionary[currentNode].neighbors.append(nodesDictionary[neighbor])
        
        return nodesDictionary[node]
        # from collections import deque

        # if not node:
        #     return None

        # visitedNodes = {}
        # visitedNodes[node] = Node(node.val)
        # queue = deque([node])

        # while queue:
        #     currentNode = queue.popleft()
        #     for neighbor in currentNode.neighbors:
        #         if neighbor not in visitedNodes:
        #             visitedNodes[neighbor] = Node(neighbor.val)
        #             queue.append(neighbor)
        #         visitedNodes[currentNode].neighbors.append(visitedNodes[neighbor])
        
        # return visitedNodes[node]
