# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []


        def dfs(node, level, res): 

            if not node:
                return 
                
            if level >= len(res):
                res.append([node.val])
            else:
                res[level].append(node.val)


            dfs(node.left, level +1 , res)


            dfs(node.right, level+1, res)
        
        dfs(root, 0, ans)
        return ans
