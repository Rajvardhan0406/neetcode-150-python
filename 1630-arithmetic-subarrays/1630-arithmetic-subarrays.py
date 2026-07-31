from typing import List

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def is_arithmetic(arr):
            arr = sorted(arr)
            diff = arr[1] - arr[0]
            for i in range(2, len(arr)):
                if arr[i] - arr[i - 1] != diff:
                    return False
            return True

        result = []
        for start, end in zip(l, r):
            subarray = nums[start:end + 1]
            result.append(is_arithmetic(subarray))

        return result