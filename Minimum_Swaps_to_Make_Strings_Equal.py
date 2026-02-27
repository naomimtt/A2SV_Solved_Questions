class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        x_y = 0
        y_x = 0
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                continue
            elif s1[i] == 'x' and s2[i] == 'y':
                x_y += 1
            else:
                y_x += 1
        if x_y % 2 != y_x % 2:
            return -1
        else:
            return (x_y // 2) + (y_x // 2) + (2 * (y_x %2 ))




        
