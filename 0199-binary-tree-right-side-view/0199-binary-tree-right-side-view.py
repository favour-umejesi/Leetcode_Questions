# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Question is asking us to return the rightmost node at each level
        inorder to get nodes at each level, I will be using BFS
        """
        queue = deque([root])
        result = []

        if not root:
            return []

        while queue:
            length = len(queue)
            result.append(queue[-1].val)

            for _ in range(length):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result

