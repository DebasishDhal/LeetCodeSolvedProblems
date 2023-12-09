#Simple in order traversal.

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def func(node):
            if node is not None:
                func(node.left)
                result.append(node.val)
                func(node.right)

        func(root)
        return result
