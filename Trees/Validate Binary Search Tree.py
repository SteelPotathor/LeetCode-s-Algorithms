from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(node, floor, ceiling):
            if not node:
                return True
            elif not floor < node.val < ceiling:
                return False
            else:
                return check(node.left, floor, node.val) and check(node.right, node.val, ceiling)

        return check(root, float("-inf"), float("inf"))