# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if (left and right): # found lowestCommonAncestor
            return root # will go to answer directly since the other side will always be None
        elif (root in {p,q}): # find one piece
            return root # will be left or right, have to go up till find the other node
        else:
            return left or right
            
        
                

