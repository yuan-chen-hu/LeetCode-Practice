# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self,root,count=0):
        count+=1        
        if root==None :
            return(True,count)
        left_count=0
        right_count=0
        left_flag=True
        right_flag=True
        
        if root.left!=None: 
            #print("to left")
            left_flag,left_count=self.check(root.left,count)  
        if root.right!=None:            
            #print("to right")
            right_flag,right_count=self.check(root.right,count)
        if left_count==0:
            #print("left end")
            left_count=count
        if right_count==0:
            #print("right end")
            right_count=count
        #print("left count=",left_count)
        #print("right count=",right_count)          
       
        if max(right_count,left_count)-min(right_count,left_count)>1:
            #print("danger")
            #print(count)
            return (False,count)
        if left_flag==False or right_flag==False:
            #print("danger2")
            #print(count)
            return (False,count)

        count=max(right_count,left_count)

           
        #print("safe")
        #print("return",count)
        return (True,count)
        
        
    def isBalanced(self, root: TreeNode) -> bool:

        return self.check(root)[0]
    
        