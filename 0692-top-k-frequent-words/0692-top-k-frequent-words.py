class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """
        Return the Top K most frequent words in the array
        M - Array, Sort
        """
        seen = {}
        for word in words:
            seen[word] = 1 + seen.get(word, 0)

        freq = []
        for key, value in seen.items():
            freq.append([-value, key])
        
        freq.sort()
        print(f"Frequecy {freq}")
        result = []
        while len(result) < k:
            result.append(freq.pop(0)[1])
        return result


        