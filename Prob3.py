# Simple Linear search algorithm
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # FOUND
    return -1  # NOT FOUND

def main():
    arr = [4, 2, 7, 8, 1, 2, 5]
    target = 90
    result = linear_search(arr, target)
    print(result)

if __name__ == "__main__":
    main()
