class Solution:
    def convertToTitle(self, n: int) -> str:
        if n<1:
            return ""
        right=n%26        
        n=int(n/26)        
        if right==0:
            right=26
            n-=1
        return self.convertToTitle(n)+chr(64+right) 
        