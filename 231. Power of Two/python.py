class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <=0:
            return False
        while(n>1):
            if n/2==int(n/2):
                n=n/2
            else:
                return False            
        return True
            

        