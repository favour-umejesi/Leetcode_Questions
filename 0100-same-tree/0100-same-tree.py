# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        A tree is equal if they are structurally identical and 
        their values are the same
        
        There are three conditions (base cases):
        - if both trees are null we return True
        - if only is empty, return False
        - if the values are not equal, return False otherwise recursively check if the left and right subtrees are equal
        """
        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return (
            self.isSameTree(p.left, q.left)
            and
            self.isSameTree(p.right, q.right)
        )
        