class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            first=nums[i]
            print("i",i)
            for k in range(i+1,len(nums)):
                print("k",k)
                if target - first == nums[k]:
                    print("return")
                    return [i,k]