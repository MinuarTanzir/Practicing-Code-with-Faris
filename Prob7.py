#Swap the max & min number of an array

arr = [3, 9, 1, 7, 5]

max_val = arr[0]
min_val = arr[0]
max_index = 0
min_index = 0

for i in range(len(arr)):
    if arr[i] > max_val:
        max_val = arr[i]
        max_index = i
    if arr[i] < min_val:
        min_val = arr[i]
        min_index = i

# Swapping
temp = arr[max_index]
arr[max_index] = arr[min_index]
arr[min_index] = temp

print("Array after swapping:", arr)
