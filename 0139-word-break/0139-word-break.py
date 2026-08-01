class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        max_len = max(len(w) for w in wordDict) 
        
        dp = [False] * (n + 1)
        dp[0] = True  
        
        for i in range(1, n + 1):
            for j in range(max(0, i - max_len), i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        
        return dp[n]