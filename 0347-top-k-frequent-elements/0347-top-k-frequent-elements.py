class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        U - Create a list containing K most frequent elements in the list
        M - Array, HashMap, Bucket-Sort
        P - Create a HashMap, to keep track of the frequency of numbers in the list
        - create list containing buckets, where the index of each bucket is the frequency of a number in the list
        - Fill the buckets by placing each number corresponding to its frequency
        - Collect the top k elements by starting from the bucket with the highest frequency.
        
        """
        freq = {}

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        bucket = [[] for i in range(len(nums)+1)]

        for key, value in freq.items():
            bucket[value].append(key)

        result = []
        n = len(nums)
        for i in range(n, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result
        