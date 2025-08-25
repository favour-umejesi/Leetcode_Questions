class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """
        Return the Top K most frequent words in the array
        M - Array, Bucket Sort
        """
        seen = {}
        n = len(words)
        for word in words:
            seen[word] = 1 + seen.get(word, 0)

        bucket = [[] for _ in range(n+1)]

        for key, value in seen.items():
            bucket[value].append(key)
        
        result = []
        for i in range(n, -1, -1):
            if bucket[i]:
                bucket[i].sort()
                for word in bucket[i]:
                    result.append(word)

                    if len(result) == k:
                        return result


        
        

        