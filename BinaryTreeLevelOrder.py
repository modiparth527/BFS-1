# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#---------------------DFS, Time = O(no of nodes), Space = O(height of tree)
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.result = []
        self.dfs(root, 0)
        return self.result
    
    def dfs(self,  root: Optional[TreeNode], lvl: int) -> None:
        # base case
        if root == None:
            return

        # logic
        if lvl == len(self.result):
            temp = []
            temp.append(root.val)
            self.result.append(temp)
        else:
            self.result[lvl].append(root.val)
        self.dfs(root.left, lvl + 1)
        self.dfs(root.right, lvl + 1)
    
#-----------------------------BFS, Time = O(n), Space= O(n/2) = O(n)
# from queue import Queue
# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         if root is None:
#             return []
#         q = Queue()
#         result = []
#         q.put(root)
#         while not q.empty():
#             size = q.qsize()
#             temp = []
#             for i in range(size):
#                 curr = q.get()
#                 temp.append(curr.val)
#                 if curr.left !=None:
#                     q.put(curr.left)
#                 if curr.right != None:
#                     q.put(curr.right)
#             result.append(temp)
#         return result

