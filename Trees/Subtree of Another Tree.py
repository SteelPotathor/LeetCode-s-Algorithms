from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self.checkSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def checkSameTree(self, root, subTree):
        if not root and not subTree:
            return True
        elif root and subTree and root.val == subTree.val:
            return self.checkSameTree(root.left, subTree.left) and self.checkSameTree(root.right, subTree.right)
        else:
            return False
