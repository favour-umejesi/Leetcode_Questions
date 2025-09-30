# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([root])
        ans = []
        
        if not root:
            return []

        while queue:
            length = len(queue)
            currMax = float("-inf")

            for _ in range(length):
                node = queue.popleft()
                currMax = max(node.val, currMax)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            ans.append(currMax)
        return ans
        
        