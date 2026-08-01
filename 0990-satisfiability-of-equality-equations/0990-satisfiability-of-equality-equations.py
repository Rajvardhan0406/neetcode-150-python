class Solution:
    def equationsPossible(self, equations: list[str]) -> bool:
        parent = list(range(26))  
        rank = [0] * 26
        
        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]  
                x = parent[x]
            return x
        
        def union(x: int, y: int) -> None:
            rx, ry = find(x), find(y)
            if rx == ry:
                return
            if rank[rx] < rank[ry]:
                rx, ry = ry, rx
            parent[ry] = rx
            if rank[rx] == rank[ry]:
                rank[rx] += 1
        
        for eq in equations:
            if eq[1] == '=':
                x = ord(eq[0]) - ord('a')
                y = ord(eq[3]) - ord('a')
                union(x, y)
        
        for eq in equations:
            if eq[1] == '!':
                x = ord(eq[0]) - ord('a')
                y = ord(eq[3]) - ord('a')
                if find(x) == find(y):
                    return False
        
        return True