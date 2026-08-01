class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        need = 1 << k         
        if len(s) < need + k - 1:
            return False      
        
        mask = need - 1       
        curr = 0
        seen = set()
        
        for i, ch in enumerate(s):
            curr = ((curr << 1) | (ch == '1')) & mask
            if i >= k - 1:      
                seen.add(curr)
                if len(seen) == need:
                    return True
        
        return len(seen) == need