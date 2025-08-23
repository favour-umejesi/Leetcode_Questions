class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        """
        U - return the minimum number of times it takes to change white blocks to black to get k consecutive number of black blocks
        M - String, Sliding window
        P - create two variables, one to keep track of W's and other keeps track of the maximum number of W's we have seen so far
        - Build the first window by looping through the first k elements
                - counts how many W's are in the window and stores count
                - sets ans == count, to store the min we have seen so far
        - Slide the window
                - For each character at S[i], we
                - remove the effect of the character that left the window, s[i-k]
                - Add the effect of the new character at s[i]
        - Update the ans with the minimum W's count so far
        - Return ans
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