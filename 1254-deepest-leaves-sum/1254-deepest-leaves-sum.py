# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])

        while queue:
            length = len(queue)
            Sum = 0 #setting Sum to zero as we move from level to level

            for _ in range(length):
                node = queue.popleft()
                Sum += node.val #as we are dequeuing nodes at a current level, keeping track of its sum

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return Sum
        