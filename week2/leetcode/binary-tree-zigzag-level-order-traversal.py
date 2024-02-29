# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        zigzag = []
        
        def BFS(root):
            queue = deque()

            if root:
                queue.append(root)
                
            level = 0
            while queue:
                vals = []

                if level % 2:
                    for i in range(len(queue)-1,-1,-1):
                        vals.append(queue[i].val)
                else:
                    for i in range(len(queue)):
                        vals.append(queue[i].val)

                zigzag.append(vals)

                for i in range(len(queue)):
                    curr = queue.popleft()
                    
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
                level += 1
        
        BFS(root)
        return zigzag
                

            
        