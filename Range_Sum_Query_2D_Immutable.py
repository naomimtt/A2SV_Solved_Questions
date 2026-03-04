class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        prefix = [[0]* len(matrix[0]) for _ in range(len(matrix))]
        self.prefix = prefix
        prefix[0][0]=matrix[0][0]
        for i in range (len(matrix)):
            for j in range (len(matrix[0])):
                if i == 0 and j == 0: 
                    continue
                if i !=0 and j!=0:
                    prefix[i][j]= prefix[i-1][j]+ prefix[i][j-1]-prefix[i-1][j-1]+ matrix[i][j]
                else:
                    if i==0:
                        prefix[i][j]= prefix[i][j-1]+ matrix[i][j]
                    else:
                        prefix[i][j]= prefix[i-1][j]+ matrix[i][j]



        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        p = self.prefix
        
        total = p[row2][col2]
        top = p[row1-1][col2] if row1 > 0 else 0
        left = p[row2][col1-1] if col1 > 0 else 0
        diag = p[row1-1][col1-1] if row1 > 0 and col1 > 0 else 0
        
        return total - top - left + diag
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
