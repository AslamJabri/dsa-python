#Basic handling
arr = [1,2,3,4]
for i in range(len(arr)):
    print(arr[i])
    
# Sum Of Elements

sum = [5,10,15]
added_sum =0
for i in range(len(sum)):
    
    added_sum += sum[i] 
print(f"Sum of all numbers: {added_sum}")


# Find Maximum Element
elements = [3, 7, 2, 9, 1]
highest_element = elements[0]
for element in elements:
    if element > highest_element:
        highest_element = element
    
print(f"Highest element : {highest_element}")

#Find Minimum Element

numbers = [8, 4, 6, 2]
minimum = numbers[0]

for num in numbers:
    if num < minimum:
        minimum = num
print(f"Minimum Number: {minimum}")

