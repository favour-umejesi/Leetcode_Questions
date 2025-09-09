class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
       
        res = 0
        for i in range(n):
            res += mat[i][i] #primary diagonal
            res += mat[i][n-1-i] #secondary diagonal

        if n % 2 != 0: #if the matrix is odd
            res -= mat[n//2][n//2] #subtract value at intersection point
        return  res
        