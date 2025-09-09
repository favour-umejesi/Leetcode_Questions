class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:

        """
        in the primary diagonal, the index of the row and column are the same
        for the secondary diagonal, the row is the same but column keeps decreasing by 1
        to ensure we don't add the intersection point value twice, we substract it from the final answer
        """

        n = len(mat)
       
        res = 0
        for i in range(n):
            res += mat[i][i] #primary diagonal
            res += mat[i][n-1-i] #secondary diagonal

        if n % 2 != 0: #if the matrix is odd
            res -= mat[n//2][n//2]
        return  res
        