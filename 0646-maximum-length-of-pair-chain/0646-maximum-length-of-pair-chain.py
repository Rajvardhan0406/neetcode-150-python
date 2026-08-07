class Solution:
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        pairs.sort(key=lambda p: p[1])  
        
        chain_len = 0
        current_end = float('-inf')
        
        for a, b in pairs:
            if a > current_end:
                chain_len += 1
                current_end = b
        
        return chain_len