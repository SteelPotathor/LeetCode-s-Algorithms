from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = []

        if root:
            queue.append(root)

        while queue:
            list = []
            for i in range(len(queue)):
                treenode = queue.pop(0)
                list.append(treenode.val)
                if treenode.left:
                    queue.append(treenode.left)
                if treenode.right:
                    queue.append(treenode.right)
            res.append(list[-1])
        return res
