class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        unique = set(nums)
        if len(nums)==len(unique):  return False
        for n in unique:
            count = nums.count(n)
            if count>1:
                first = nums.index(n)
                while count>1:
                    second = nums[first+1:].index(n)+1
                    if second<=k:
                        return True
                    first+=second
                    count-=1
            
        return False