#Even Number of Elements

def reverse_array(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

# Even-sized array
arr = [10, 20, 99, 40, 56, 60]
reverse_array(arr)

print("Reversed :", arr)
