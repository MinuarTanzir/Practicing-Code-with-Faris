#WAF to swap the max & min number of an array

def swap_max_min(arr):
    if not arr:
        return arr
    max_val = max(arr)
    min_val = min(arr)
    max_index = arr.index(max_val)
    min_index = arr.index(min_val)
    arr[max_index], arr[min_index] = arr[min_index], arr[max_index]
    print("Array after swapping max and min:", arr)
