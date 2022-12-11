from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def averageOfLevels(root: TreeNode) -> List[float]:
    stack = [root]
    res = []
    while stack:                       
        tem = []                       
        value = 0                      
        for i in stack:                
            if i.left:                 
                tem.append(i.left)     
            if i.right:                
                tem.append(i.right)
            value += i.val             
        res.append(value / len(stack)) 
        stack = tem[:]                 
    return res   