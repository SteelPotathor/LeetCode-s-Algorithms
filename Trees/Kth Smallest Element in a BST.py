from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res=[]
        def traversal(node):
            if node:
                traversal(node.left)
                res.append(node.val)
                traversal(node.right)

        traversal(root)
        return res[k - 1]


sol = Solution()
l = TreeNode(3, TreeNode(1, None, TreeNode(2, None, None)), TreeNode(4, None, None))

print(sol.kthSmallest(l, 1))