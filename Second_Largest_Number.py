Question = "Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1. Note: The second largest element should not be equal to the largest element."

#Solution 1 - Naive Approach (Sorting the array). Time complexity- O(n*log n), Space Complexity- O(1)
class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        n = len(arr)     #Naive approach
        arr.sort()
        for i in range(n-2,-1,-1):
            if arr[i] != arr[n-1]:
                return arr[i]
                
        return -1


#Solution 2- Better Approach (Traversing through the List Twice), O(n) time and O(1) Space
class solution:
	def getSecondLargest(self, arr):
        # Code Here
        n = len(arr)     #Better approach
        second_largest = -1
        largest_number = -1
        
        for i in range(n):#find the largest number
            if arr[i] > largest_number:
		    largest_number = arr[i]
                
        
        #tranverse through the list to find the second_largest number
        for i in range(n):
            if arr[i] > second_largest and arr[i] != largest_number:
                second_largest = arr[i]
                
        return second_largest


#Solution 3 - Expected Approach (Transversing through the list once) O(n) time and O(1) Space
class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        n = len(arr)     #Expected approach
        second_largest = -1
        largest_number = -1
        
        for i in range(n):  #Transversing through the list once
            if arr[i] > largest_number:
                second_largest = largest_number
                largest_number = arr[i]
                
            if arr[i] > second_largest and arr[i] != largest_number:
                second_largest = arr[i]
                
        return second_largest
