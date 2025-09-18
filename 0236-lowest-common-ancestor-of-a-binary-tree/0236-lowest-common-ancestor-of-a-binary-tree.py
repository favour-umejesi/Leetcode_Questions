# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        - The root node is p or q, then the descendant can't be below, return the current node
        - One of p or q is in the left subtree, and the other one is in the right subtree. The root must be the answer 
        - Both p and q are in one of the subtrees, return the current node
        """
        if not root:
            return None
        if p == root or q == root:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        if left:
            return left

        return right