from typing import List
from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]] 
                x = parent[x]
            return x

        def union(x, y):
            root_x, root_y = find(x), find(y)
            if root_x != root_y:
                parent[root_x] = root_y

        email_to_name = {}

        for account in accounts:
            name = account[0]
            first_email = account[1]
            if first_email not in parent:
                parent[first_email] = first_email
            email_to_name[first_email] = name

            for email in account[2:]:
                if email not in parent:
                    parent[email] = email
                email_to_name[email] = name
                union(first_email, email)

        groups = defaultdict(list)
        for email in parent:
            root = find(email)
            groups[root].append(email)

        result = []
        for root, emails in groups.items():
            name = email_to_name[root]
            result.append([name] + sorted(emails))

        return result