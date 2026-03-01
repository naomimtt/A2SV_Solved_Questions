class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)
        my_coins = 0
        index = n - 2
        for _ in range(n // 3):
            my_coins += piles[index]
            index -= 2
        return my_coins
