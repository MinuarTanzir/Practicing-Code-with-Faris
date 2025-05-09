#Print intersection of 2 arrays using nested loops

arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 6, 7]

print("Intersection:")
for i in range(len(arr1)):
    for j in range(len(arr2)):
        if arr1[i] == arr2[j]:
            print(arr1[i])
            break  # Optional: prevents repeated printing if duplicates exist
