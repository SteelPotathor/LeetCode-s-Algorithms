from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        def dfs(node):
            nonlocal res
            if not node:
                return 0
            else:
                left = max(dfs(node.left),0)
                right = max(dfs(node.right),0)
                res = max(res, node.val + left + right)
                return node.val + max(left, right)

        dfs(root)
        return res


sol = Solution()
l = TreeNode(1, TreeNode(2, None, None), TreeNode(3, None, None))
t = TreeNode(-10, TreeNode(9, None, None), TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None)))

print(sol.maxPathSum(l))
print(sol.maxPathSum(t))
