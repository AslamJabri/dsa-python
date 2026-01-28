# Q1. Find the maximum element in an array

find_max_element = [3,7,1,9,4]

def max_element(arr):
    max_value = arr[0]
    for num in arr:
        if num > max_value:
            max_value = num
            
    return max_value

print(max_element(find_max_element))