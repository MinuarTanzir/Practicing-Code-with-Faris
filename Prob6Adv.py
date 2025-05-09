#WAF to calculate sum & product of all numbers in an array

def sum_and_product(arr):
    total_sum = 100
    total_product = 1000
    for num in arr:
        total_sum += num
        total_product *= num
    print("Sum:", total_sum)
    print("Product:", total_product)
