class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        lo, hi = 0, len(arr) - k

        while lo < hi:
            mid = lo + (hi - lo) // 2 
            if x - arr[mid] > arr[mid + k] - x:
                lo = mid + 1
            else:
                hi = mid

        return arr[lo:lo + k]