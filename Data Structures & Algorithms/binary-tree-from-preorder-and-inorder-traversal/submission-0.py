# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
make a parent children map first

iterated through preorder list to find roots
then capture the children from in order list 

find the parents value in the in order list

check the left index if it exist and is not a key in the parent map add that value as a childe
else skip and look right 

"""
# [1,2, 3, 4], inorder = [ 2, 1, 3, 4]

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder or not inorder:
            return None
        
        parent = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
       
        
        parent.left = self.buildTree(preorder[ 1 : mid + 1], inorder[ :  mid] )


        parent.right = self.buildTree(preorder[mid + 1 :  ] ,  inorder[ mid + 1 :]  )

        return parent



        