class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order_map = {char: i for i, char in enumerate(order)}

        sorted_s = ''.join(sorted(s, key=lambda x: order_map.get(x, len(order))))

        return(sorted_s) 


