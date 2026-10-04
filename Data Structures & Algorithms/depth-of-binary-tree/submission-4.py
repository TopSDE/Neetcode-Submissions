# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        return max(l, r) + 1

'''
"FCPBD"
FULL B.T
COMPLETE B.T
PERFECT B.T
BALANCED B.T
DEGENERATE B.T

FULL BINARY TREE = where every node has either zero or two children.
COMPLETE BINARY TREE = 
1) where all levels are filled completely except possibly the last level
2) The last level needs to be filled from left to right.
PERFECT B.T = All leaf nodes needs to be in the same level and every parent has two children.
BALANCED B.T = Height of tree at max log2(N)
DEGENERATE B.T = Every node has a single child 

--------------------------------------
FOR BALANCED B.T = 
Here Height = No. of Nodes
1) 2^h = n
2) log₂(2^h) = log₂(n)
    -> log₂(2^h) = h
3) h = log₂(n)

FOR MORE INFO LIKE WHY DFS S.C IS LOG2(N) FOR BALANCED B.T AND O(N) FOR SKEWED TREE: https://chatgpt.com/c/688c02ea-7b70-8000-abc9-fbbb72e09d00

--------------------------------------
if not preorder:
    return None
The above code handles both:
->preorder = None
->preorder = [ ] (empty list)
'''