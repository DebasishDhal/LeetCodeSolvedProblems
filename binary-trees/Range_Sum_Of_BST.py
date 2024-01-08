# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#Get the sum of all nodes if they fall within a range.

class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
    def __init__(self):
        self.count = 0

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root:
            item = root.val if low <= root.val <= high else 0
            self.count += item
            print(root.val, self.count)
            self.rangeSumBST(root.left, low, high)
            self.rangeSumBST(root.right, low, high)
        return self.count
