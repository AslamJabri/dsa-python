#Find the second largest element in an array.
arr = [10, 5, 20, 8]

def second_largest(arr):
    largest = float('-inf')
    second = float('-inf')
 
    for x in arr:
        if x > largest:
            second = largest
            largest = x
        elif x < largest and x > second:
                second = x
                
    return second
            
          
          
        
print(second_largest(arr))


#Count how many elements are greater than a given value k.

arr_count = [3, 7, 1, 9, 4]
k = 4

def count_greater_number(arr,k):
    count = 0
    for x in arr:
        if k > x:
            count+=1
    return count
print(count_greater_number(arr_count,k))

#Check if an array is sorted in non-decreasing order.
non_decreasing_order = [1,2,2,5,7]

def non_decreasing(arr):
    
    for x in range(len(arr)-1):
        if arr[x+1] < arr[x]:
            return False
    return True
        
        
print(non_decreasing(non_decreasing_order))

# #Reverse the array in-place.
sorted_array = [1,2,3,4]

def reverse_array(arr):
    left = 0
    right = len(arr)-1
    
    while left < right:
        arr[left],arr[right] = arr[right],arr[left]
        left +=1
        right -=1
    return arr
   
        
print(reverse_array(sorted_array))