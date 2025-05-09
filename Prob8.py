#Print all the unique values in an array

arr = [1, 2, 2, 3, 4, 1, 5]

print("Unique values:")
for i in range(len(arr)):
    count = 0
    for j in range(len(arr)):
        if arr[i] == arr[j]:
            count = count + 1
    if count == 1:
        print(arr[i])
