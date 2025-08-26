class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        U - Find the overlapping intervals in the list
        For instance we have [1,3], [2,6] --> [2,3] can be found in [1,6]
        M - Array, Sortinh
        P - 1.	Sort the intervals by their starting values.
	        This ensures we always process intervals in the correct order, so overlaps are easy to detect.
	2.	Initialize the result list merged with the first interval.
	        This gives us a starting point to compare against.
	3.	Loop through the remaining intervals one by one:
	        Compare the current interval’s start with the end of the last merged interval.
	        If the current start is less than or equal to the last merged end → the intervals overlap.
	        Update the end of the last merged interval to the maximum of the two end values.
	        Otherwise (no overlap) → append the current interval to merged as a new entry.
	4.	Return the merged list after processing all intervals.
        """
        intervals.sort()
        merged = [intervals[0]]

        for left, right in intervals[1:]:
            if merged[-1][1] >= left:
                merged[-1][1] = max(merged[-1][1], right)
            else:
                merged.append([left, right])
        return merged