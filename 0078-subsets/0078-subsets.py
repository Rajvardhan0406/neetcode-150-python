class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        current = []

        def backtrack(index: int) -> None:
            result.append(current[:])

            for i in range(index, len(nums)):
                current.append(nums[i])
                backtrack(i + 1)
                current.pop()

        backtrack(0)
        return result