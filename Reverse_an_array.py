#Given an array arr[], the task is to reverse the array. Reversing an array means rearranging the elements such that the first element becomes the last, the second element becomes second last and so on.
#Solution 1- [Naive Approach] Using a temporary array - O(n) Time and O(n) Space
class Solution:
    def reverseArray(self, arr): #using a naive approach
        n = len(arr)
        temp = [0]*n
## Copy elements from original array to temp in reverse order
        for i in range(n):
            temp[i] = arr[n-1-i] #access elements of the array in reverse order
#Copy the elements back into the initial array
        for i in range(n):
            arr[i] = temp[i]
        return arr


#Solution 2- [Expected Approach - 1] Using Two Pointers - O(n) Time and O(1) Space

class Solution:
  def reverseArray(self, arr): 
    n = len(arr)
    i = 0
    j = n-1

#Create a condition to iterate through the list till left becomes greater than right (index, e.g index 5 > index 4)
      while i < j:
        arr[i],arr[j] = arr[j],arr[i]
        i += 1 #increment the left by 1
        j -= 1 #descrement the left by 1
      return arr

#Solution 3- Using Inbuilt Methods - O(n) Time and O(1) Space
class Solution:
  def reverseArray(self,arr):
    temp_arr = arr.reverse()
    
    return arr



