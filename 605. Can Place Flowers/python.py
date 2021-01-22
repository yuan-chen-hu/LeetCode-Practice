class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        total=0
        combo=0
        flowerbed=[0]+flowerbed+[0,1]
        print(flowerbed)
        for i in range(0,len(flowerbed)):
            if flowerbed[i]==0:           
                combo+=1
            else:
                total+=int((combo-1)/2)
                combo=0
                    
        if total>=n:
            return True
        else : 
            return False
        