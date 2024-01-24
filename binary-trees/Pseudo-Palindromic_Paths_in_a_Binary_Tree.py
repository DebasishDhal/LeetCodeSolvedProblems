'''
For a given binary tree, find out how many paths starting from the top node to leaf node are pseudo-palindromic.
This is divided into two parts. First problem is find all the paths starting from top node and ending at every leaf node.
Second part is deciding which path list can be pseudo-palindromic. For pseudo-palindromic, the condition is that at most one number has an odd number of occurence. 
'''

#My first attempt
class Solution:
    def get_all_paths(self, root: Optional[TreeNode]): #Get all the paths
        result = []
        if root is None:
            return result

        def dfs(node, path):
            if node.left is None and node.right is None:
                result.append(path + [node.val])
                return

            if node.left:
                dfs(node.left, path + [node.val])
            if node.right:
                dfs(node.right, path + [node.val])

        dfs(root, [])
        return result

    def isPalindrome(self, path): #Decide whether a path is palindromic or not
        count = {}
        for item in path:
            if item not in count:
                count[item] = 1
            else:
                count[item] += 1
        odd_count = len([occurence for occurence in count.values() if occurence %2 !=0])
        return odd_count <=1
        
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int: #Main function
        paths = self.get_all_paths(root)
        return sum([self.isPalindrome(path) for path in paths]) 

#Notice the problem? The numbers of nodes in this binary tree can go till 10**5. Hence it crosses the memory quota.
#In the next try, we don't store the paths, we just calculate it on the go.

class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.count = 0

        def dfs(node, path_count):
            if not node:
                return

            path_count[node.val] += 1

            if not node.left and not node.right:
                odd_count = sum(occurrence % 2 for occurrence in path_count.values())
                if odd_count <= 1:
                    self.count += 1

            dfs(node.left, path_count.copy())
            dfs(node.right, path_count.copy())

        dfs(root, defaultdict(int))
        return self.count
