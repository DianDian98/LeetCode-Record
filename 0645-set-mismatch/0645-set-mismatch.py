class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        num, replace = None, None
        nums = sorted(nums)
        for i in range(len(nums)-1):
            if num==None and nums[i]==nums[i+1]:
                num = nums[i]
                if replace!=None: return [num, replace]   
            if replace==None and i+1 not in nums:
                replace = i+1
                if num!=None: return [num, replace]
        
        return [num,len(nums)]