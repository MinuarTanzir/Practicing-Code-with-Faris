# find the smallest & largest values

nums = [5, 15, 22, 1, -15, -24]

# Initialize smallest and largest
smallest = float('inf')
largest = float('-inf')

for num in nums:
    smallest = min(num, smallest)
    largest = max(num, largest)

print("smallest =", smallest)
print("largest =", largest)


