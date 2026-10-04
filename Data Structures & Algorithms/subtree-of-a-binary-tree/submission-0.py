# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True

        elif (not p or not q) or (p.val != q.val):
            return False

        l = self.isSameTree(p.left, q.left)
        r = self.isSameTree(p.right, q.right)

        return l and r
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        check = False
        if root.val == subRoot.val:
            check = self.isSameTree(root, subRoot)

        l = self.isSubtree(root.left, subRoot)
        r = self.isSubtree(root.right, subRoot)

        return check or l or r