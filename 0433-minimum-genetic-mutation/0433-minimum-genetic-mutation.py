from typing import List
from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank_set = set(bank)
        if endGene not in bank_set:
            return -1

        genes = ['A', 'C', 'G', 'T']
        visited = {startGene}
        queue = deque([(startGene, 0)])

        while queue:
            gene, mutations = queue.popleft()

            if gene == endGene:
                return mutations

            for i in range(len(gene)):
                for c in genes:
                    if c != gene[i]:
                        mutated = gene[:i] + c + gene[i+1:]
                        if mutated in bank_set and mutated not in visited:
                            visited.add(mutated)
                            queue.append((mutated, mutations + 1))

        return -1