from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not preorder:
            return None
        else:
            root = TreeNode(preorder[0])
            mid = inorder.index(preorder[0])
            print(mid)
            root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
            root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
            return root


sol = Solution()
sol.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
