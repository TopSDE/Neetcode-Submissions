# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        while curr:
            if (p.val <= curr.val <= q.val) or (p.val >= curr.val >= q.val):
                return curr

            elif p.val < curr.val:
                curr = curr.left
            
            else:
                curr = curr.right