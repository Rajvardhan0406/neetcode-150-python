class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        result = []
        path = []
        n = len(candidates)

        def backtrack(start: int, remaining: int) -> None:
            if remaining == 0:
                result.append(path[:])
                return
            if remaining < 0:
                return

            for i in range(start, n):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > remaining:
                    break

                path.append(candidates[i])
                backtrack(i + 1, remaining - candidates[i])
                path.pop()

        backtrack(0, target)
        return result