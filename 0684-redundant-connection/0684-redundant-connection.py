class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges)
        parent = list(range(n + 1))  
        rank = [0] * (n + 1)
        
        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]  
                x = parent[x]
            return x
        
        def union(x: int, y: int) -> bool:
            root_x, root_y = find(x), find(y)
            if root_x == root_y:
                return False  
            
           
            if rank[root_x] < rank[root_y]:
                root_x, root_y = root_y, root_x
            parent[root_y] = root_x
            if rank[root_x] == rank[root_y]:
                rank[root_x] += 1
            return True
        
        for u, v in edges:
            if not union(u, v):
                return [u, v]
        
        return []  