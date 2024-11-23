#Given an array arr[]. Push all the zeros of the given array to the right end of the array while maintaining the order of non-zero elements. Do the mentioned change in the array in place.
#Input = [40503044]  #Expected_output = [45344000]

#Solution 1 - Naive approach (Transverse through the array 3 times) Time Complexity = O(n), Space_Complexity = O(n)
class solution:
  def pushZeroestotheEnd(self,arr):
	  n = len(arr)
	  temp_arr = [0] * n
	  j = 0
	 

#Transverse through the list and copy the non-zeroes element to the temporary array
	for i in range(n):
		if arr[i] != 0:
			temp_arr[j] = arr[i]
			j += 1

#Transverse through the list a second time to add the zero elements.
	while j < n:
		temp_arr[j] = 0
		j += 1
		
#copying the elements from temp_arr to the original arr
	for i in range(n):
		arr[i] = temp_arr[i]


#Solution 2 - Better Approach (Transverse through the array twice). Time Complexity = O(n), Space_Complexity = O(1)

class Solution:
	def PushZeroesToEnd(self,arr):
		n = len(arr)
		count = 0 #Pointer to keep track of the position of the non-zero elements
		#transverse through the list to bring the non-zero elements to the beginning of the array
		for i in range(n):
			if arr[i] != 0:
				arr[count] = arr[i]
				count += 1
		#transverse through the list to add the non-zero elements to the end of the array
		while count < n:
			if arr[count] = 0:
				count += 1

#Solution 3 - Expected Approach(Transversing through the array once). Time_Complexity = O(n), Space_Complexity = O(1)
class Solution:
	def PushZeroesToEnd(self,arr):
		n = len(arr)
		count = 0 #Pointer to keep track of the position of non_zero elements
		#Transverse through the array once, by swapping non_zero element with arr[count]
		for i in range(n):
			if arr[i] != 0:
				arr[i], arr[count] = arr[count], arr[i]
				count += 1
				


			
			
		


	
		


		

 
		
  
  
    
