class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A)!=len(B):
            return False
        old=None
        if A==B:
            C=sorted(A)
            for i in C:
                if old==i:
                    return True  
                old=i                
            return False
        count=0
        storeA=[]
        storeB=[]
        
        for i in range(len(A)):
            if A[i]!=B[i]:
                count+=1
                storeA.append(A[i])
                storeB.append(B[i])  
                if count>2:
                    return False

        if count==2:
            if storeA[0]not in storeB :
                return False
            if storeA[1]not in storeB :
                return False
            return True
        
        
        