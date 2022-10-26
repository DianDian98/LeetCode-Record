class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hash_table = {0: 0}
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            if s%k not in hash_table:
                hash_table[s%k] = i + 1
            elif hash_table[s%k]<i:
                return True
        return False