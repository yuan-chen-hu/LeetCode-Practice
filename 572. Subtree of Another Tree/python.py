# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self,s,t):
        
        if s==None and t == None:
            #print("none and none")
            return True 
        if s==None or t == None:
            #print("none or none")
            return False
        if s.val!=t.val:
            return False
        #print("go check left")
        check_left=self.check(s.left,t.left)
        #print("go check_left=",check_left)

        #print("go check right")
        check_right=self.check(s.right,t.right)
        #print("go check_right=",check_right)            

        if  check_left and check_right :
            #print("if if")
            return True
            
                
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        
        if s==None:
            return False
        #print("now=",s.val)   
        if s.val==t.val:
            #print("checking ")
            if self.check(s,t)==True:
                #print("found")
                return True
            #print("checked")
        #print("go left")
        go_left=self.isSubtree(s.left,t)
        #print("go left=",go_left)

        #print("go right")
        go_right=self.isSubtree(s.right,t)
        #print("go right=",go_right)
        return  go_left or go_right     
