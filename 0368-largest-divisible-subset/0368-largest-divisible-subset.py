class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        if not nums:
            return []
        
        nums.sort()
        n = len(nums)
        dp = [1] * n      
        prev = [-1] * n   
        
        max_len = 1
        max_idx = 0
        
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
            
            if dp[i] > max_len:
                max_len = dp[i]
                max_idx = i
        
        result = []
        idx = max_idx
        while idx != -1:
            result.append(nums[idx])
            idx = prev[idx]
        
        return result[::-1]