# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def height(node):
            #base case, if it is a leaf return 0, recursively backtrack
            if not node:
                return 0

            #checking for longest left and right subtree
            left = height(node.left)
            right = height(node.right)

            #keep track of longest path passing current node
            self.diameter = max(self.diameter, left+right)

            #height of subtree
            return 1 + max(left, right)

        height(root)
        return self.diameter
        