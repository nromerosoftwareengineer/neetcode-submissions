# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:



        def dfs(node, integers): 

            if not node:
                return None


            dfs(node.left, integers)
            integers.append(node.val)
            dfs(node.right, integers)


        ans = []


        dfs(root, ans)
        for i in range(len(ans)): 
            k -=1
            if k == 0:
                return ans[i]
        return -1
        