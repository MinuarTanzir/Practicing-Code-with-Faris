#Calculate sum & product of all numbers in an array

arr = [1, 2, 3, 4, 5]

sum = 0
product = 1

for i in arr:
    sum = sum + i
    product = product * i

print("Sum:", sum)
print("Product:", product)
