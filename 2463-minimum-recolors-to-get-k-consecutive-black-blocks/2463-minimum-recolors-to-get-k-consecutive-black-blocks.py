class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        """
        U - return the minimum number of times it takes to change white blocks to black to get k consecutive number of black blocks
        M - String, Sliding window
        P - create 

        """
        count, ans = 0, 0
        for i in range(k):
            if blocks[i] == "W":
                count += 1
        ans = count
        for i in range(k, len(blocks)):
            if blocks[i-k] == "W":
                count -= 1
            if blocks[i] == "W":
                count += 1
            
            
            ans = min(ans, count)


        return ans