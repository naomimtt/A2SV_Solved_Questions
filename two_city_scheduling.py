class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        cost = sorted(costs, key = lambda x: x[0]-x[1])
        expense = 0
        for i in range(len(cost)//2):
            expense += cost[i][0]
        for i in range(len(cost)//2, len(cost)):
            expense += cost[i][1]
        return expense
