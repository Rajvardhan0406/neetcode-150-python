from typing import List

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False

        s1_count = [0] * 26
        window_count = [0] * 26

        for i in range(n):
            s1_count[ord(s1[i]) - ord('a')] += 1
            window_count[ord(s2[i]) - ord('a')] += 1

        if s1_count == window_count:
            return True

        for i in range(n, m):
            window_count[ord(s2[i]) - ord('a')] += 1
            window_count[ord(s2[i - n]) - ord('a')] -= 1

            if s1_count == window_count:
                return True

        return False