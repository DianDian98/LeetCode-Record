class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        unique = set(nums)
        # nums全部不同
        if len(nums)==len(unique):  return False
        for n in unique:
            count = nums.count(n)
            # 只計算含2個以上的元素
            if count>1:
                first = nums.index(n)
                while count>1:
                    # 和下一個重複元素的間隔
                    second = nums[first+1:].index(n)+1
                    if second<=k:
                        return True
                    first+=second
                    count-=1
            
        return False