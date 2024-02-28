# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        # mp = defaultdict(int)
        # def traverse(root):
        #     if root == None:
        #         return
        #     mp[root.val] += 1
        #     traverse(root.left)
        #     traverse(root.right)

        # traverse(root)

        # vals = []
        # maxx = 0
        # for key in mp:
        #     if mp[key] > maxx:
        #         vals = [key]
        #         maxx = mp[key]
        #     elif mp[key] == maxx:
        #         vals.append(key)
        # return vals
        currentVal, maxxMode, modes, currMode = None, 0, [], 0
        def traverse(root):
            nonlocal currentVal, maxxMode, modes, currMode
            if root == None:
                return

            if root:
                traverse(root.left)

                if root.val == currentVal:
                    currMode += 1
                else:
                    currentVal = root.val
                    currMode = 1
                    
                if currMode > maxxMode:
                    maxxMode = currMode
                    modes = [currentVal]
                elif currMode == maxxMode:
                    modes.append(currentVal)

                traverse(root.right)
        
        traverse(root)

        return modes


        