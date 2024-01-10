# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
You are given the root of a binary tree with unique values, and an integer start. At minute 0, an infection starts from the node with value start. Each minute, a node becomes infected if:

The node is currently uninfected.
The node is adjacent to an infected node.
Return the number of minutes needed for the entire tree to be infected.

#Infection doesn't differentiate between parent and childrens. So the binary tree should be converted into a bidirectional graph.
#In a bidrectional graph, for every node as key, the values will be all the nodes that are connected to it.
#Then we start the infection
'''
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
      
        graph = {} 
        queue = [(root, None)]  #we start with root and None as its parent
        while len(queue) > 0:
            node, parent_val = queue.pop(0)
            graph[node.val] = [parent_val] if parent_val is not None else []
            if node.left:
                graph[node.val].append(node.left.val)
                queue.append((node.left, node.val))  #parent information of left wala node
            if node.right:
                graph[node.val].append(node.right.val)
                queue.append((node.right, node.val))  #parent information of right wala node
        
        keys = list(graph.keys())
        infected = set([start])
        current = [start]
        count = 0

        while len(infected) < len(keys):
            nodes= []
            for key in current:
                nodes.extend(graph[key])
            current = [node for node in nodes if node not in infected]
            infected.update(current)
            count += 1
        
        return count

