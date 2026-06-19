# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque()
        q.append(root)
        while q:
            li = []
            for i in range(len(q)): # Go through all nodes in level
                node = q.popleft()
                if node: # Only perform operations when node is not null
                    li.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if li: # Only add non empty levels/lists
                res.append(li)
        return res
        