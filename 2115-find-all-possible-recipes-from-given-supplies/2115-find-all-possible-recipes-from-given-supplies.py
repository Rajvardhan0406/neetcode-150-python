class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        in_degree = {r: 0 for r in recipes}
        supply_set = set(supplies)

        for i, recipe in enumerate(recipes):
            for ing in ingredients[i]:
                if ing not in supply_set:
                    graph[ing].append(recipe)
                    in_degree[recipe] += 1

        queue = deque(supplies)
        result = []

        for r in recipes:
            if in_degree[r] == 0:
                result.append(r)
                queue.append(r)

        while queue:
            item = queue.popleft()
            for recipe in graph[item]:
                in_degree[recipe] -= 1
                if in_degree[recipe] == 0:
                    result.append(recipe)
                    queue.append(recipe)

        return result