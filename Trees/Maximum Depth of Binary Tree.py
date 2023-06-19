from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        width = 0

        # Calculate the height of each treenode
        def dfs(root):
            nonlocal width

            if not root:
                return -1
            else:
                left = dfs(root.left)
                right = dfs(root.right)
                width = max(left + right + 2, width)
                return max(left, right) + 1

        dfs(root)
        return width
