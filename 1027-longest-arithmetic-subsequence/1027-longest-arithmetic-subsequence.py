class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        
        dp = [dict() for _ in range(n)]
        longest = 2

        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                prev_len = dp[j].get(diff, 1)
                dp[i][diff] = prev_len + 1
                longest = max(longest, dp[i][diff])

        return longest