# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        """
        Find the maximum difference between an ancestor node and its descendant node
        Using an helper function with extra inputs, currMax to keep track of max value seen along the path from the root to the current node, and currMin keeps 
        track of the minimum value seen along the path

        """
        def dfs(node, currMax, currMin):
            if not node:
                return currMax - currMin

            currMax = max(currMax, node.val)
            currMin = min(currMin, node.val)

            left = dfs(node.left, currMax, currMin)
            right = dfs(node.right, currMax, currMin)

            return max(left, right)

        return dfs(root, root.val, root.val)