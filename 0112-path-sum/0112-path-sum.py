"""
U - Find a path in the tree, where the root-leaf sums up to target
M - Binary Tree
P - 1) if there is no root, return false
    2) if we have reached the end of the tree, left or right, we check if the node value is equal to what is left of target.
    3) hasPathSum(root.left, targetSum - root.val) or hasPathSum(root.right, targetSum - root.val)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right:
            return root.val == targetSum

        return (
            self.hasPathSum(root.left, targetSum - root.val)
            or
            self.hasPathSum(root.right, targetSum - root.val)
        )
    
        