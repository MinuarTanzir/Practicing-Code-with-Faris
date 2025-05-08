# find the smallest & largest index Number

nums = [5, 15, 22, 1, -15, -24]

smallest = min(nums)
largest = max(nums)

smallest_index = nums.index(smallest)
largest_index = nums.index(largest)

print("smallest at index", smallest_index)
print("largest at index", largest_index)
