class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        result = []
        i, j = 0, 0
        
        while i < len(firstList) and j < len(secondList):
            start_a, end_a = firstList[i]
            start_b, end_b = secondList[j]
            
            overlap_start = max(start_a, start_b)
            overlap_end = min(end_a, end_b)
            
            if overlap_start <= overlap_end:
                result.append([overlap_start, overlap_end])
            
            if end_a < end_b:
                i += 1
            else:
                j += 1
        
        return result