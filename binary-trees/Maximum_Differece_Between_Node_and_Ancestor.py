'''
There's a binary tree. Not a search tree. You have the find the largest possible difference between an ancestor and any of its descendents (and not just its children).
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_subtree_min_max(self, root): #For every node as key in dictionary result, it adds max and min of all descendents of that node as the value. It includes the node too.
        def dfs(node):
            if not node:
                return (float('inf'), float('-inf'))

            left_min, left_max = dfs(node.left)
            right_min, right_max = dfs(node.right)

            subtree_min = min(node.val, left_min, right_min)
            subtree_max = max(node.val, left_max, right_max)

            result[node.val] = (subtree_min, subtree_max)

            return subtree_min, subtree_max

        result = {}
        dfs(root)
        return result
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        minMaxDict = self.find_subtree_min_max(root)
        # print(minMaxDict)
        minMaxDict = [max(abs(val[1]-key),abs(val[0]-key)) for key,val in minMaxDict.items()]
        # print(minMaxDict)
        # return 0
        return max(minMaxDict)

  #Example of minMaxDict for [8,3,10,1,6,null,14,null,null,4,7,13]= {1: (1, 1), 4: (4, 4), 7: (7, 7), 6: (4, 7), 3: (1, 7), 13: (13, 13), 14: (13, 14), 10: (10, 14), 8: (1, 14)}. 
  #Here 1 is a leaf here, thus 1 is the min and the max value.

'''
JavaScript solution
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
function findSubtreeMinMax(root) {
    const result = {};

    function dfs(node) {
        if (!node) {
            return [Infinity, -Infinity];
        }

        const [leftMin, leftMax] = dfs(node.left);
        const [rightMin, rightMax] = dfs(node.right);

        const subtreeMin = Math.min(node.val, leftMin, rightMin);
        const subtreeMax = Math.max(node.val, leftMax, rightMax);

        result[node.val] = [subtreeMin, subtreeMax];

        return [subtreeMin, subtreeMax];
    }

    dfs(root);

    return result;
} 
var maxAncestorDiff = function(root) {
    const minMaxDict = findSubtreeMinMax(root)
    // console.log(minMaxDict)
    const differences = Object.keys(minMaxDict).map(key => {
        const [subtreeMin, subtreeMax] = minMaxDict[key];
        return Math.max(Math.abs(subtreeMax - key), Math.abs(subtreeMin - key));
    });

    return Math.max(...differences);
};
'''

'''
TypeScript solution
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */
function findSubtreeMinMax(root) {
    const result = {};

    function dfs(node) {
        if (!node) {
            return [Infinity, -Infinity];
        }

        const [leftMin, leftMax] = dfs(node.left);
        const [rightMin, rightMax] = dfs(node.right);

        const subtreeMin = Math.min(node.val, leftMin, rightMin);
        const subtreeMax = Math.max(node.val, leftMax, rightMax);

        result[node.val] = [subtreeMin, subtreeMax];

        return [subtreeMin, subtreeMax];
    }

    dfs(root);

    return result;
} 
function maxAncestorDiff(root: TreeNode | null): number {
    const minMaxDict = findSubtreeMinMax(root)
    const differences = Object.keys(minMaxDict).map(key => {
        const [subtreeMin, subtreeMax] = minMaxDict[key];
        return Math.max(Math.abs(subtreeMax - key), Math.abs(subtreeMin - key));
    });

    return Math.max(...differences);
};
'''
