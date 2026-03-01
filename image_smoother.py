class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        neighbors = [(0,0),(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]
        rows = len(img)
        cols = len(img[0])
        img2 = [[0 for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                total = 0
                n = 0
                for l,r in neighbors:
                    if i + l >= 0 and i + l < rows:
                        if j + r >= 0 and j + r < cols:
                            total += img[i+l][j+r]
                            n+=1
                    img2[i][j]= total//n
        return img2
