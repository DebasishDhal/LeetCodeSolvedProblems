'''
Given two binary trees, return True if and only if the sequence made their leaf nodes are the same
'''

class Solution:
    def leaf_traversal(self, root):
        leafList = []
        if root is None:
            return []
        if root.right is None and root.left is None:
            leafList.append(root.val)
        leafList.extend(self.leaf_traversal(root.left))
        leafList.extend(self.leaf_traversal(root.right))
        return leafList

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:        
        ll1 = self.leaf_traversal(root1)
        ll2 = self.leaf_traversal(root2)
        # print(ll1)
        # print(ll2)
        
        return ll1 == ll2
