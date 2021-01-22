class Solution:
    def __init__(self):        
        self.history=[]
    def isHappy(self, n: int) -> bool:
        if n in self.history:
            return False
        self.history.append(n)
        nums=[]
        total=0
        while (n>=1):
            nums.append(n%10)
            n=int(n/10)
        for i in nums:
            total+=(i**2)
        if total==1:
            return True
        else:
            return self.isHappy(total)

 

            
            
            
        