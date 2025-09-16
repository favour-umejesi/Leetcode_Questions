# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        base case: if node is empty return 0 (has no children)
        Using post-order traversal, we check the children node before the root node
        we check the left subtree for number of nodes, same for right subtree,
        take the maximum and add one, we do that till we traverse the whole tree
        """
        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return 1 + max(left, right)