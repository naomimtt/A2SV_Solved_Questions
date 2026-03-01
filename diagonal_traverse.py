class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        count = {k: [] for k in range(len(mat[0]) + len(mat) - 1)}
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                count[i + j].append(mat[i][j])
        result = []
        for k in count:
            if k % 2 == 0:
                result.extend(count[k][::-1])  
            else:
                result.extend(count[k])
        
        return result


        
        
