class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        print(nums)
        count_one=0
        count_two=0
        if len(nums)==1:
            return True
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]: 
                count_one+=1
                if count_one>1:
                    return False
                if(i-1)>=0:
                    for k in range(i,len(nums)-1):
                        if nums[k-1]>nums[k+1]:                           
                            count_two+=1
                            if count_two>1:
                                return False                                  
        return True            
        