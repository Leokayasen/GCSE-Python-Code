import time


def BubbleSort(a):
    n = len(a)
    # Traverse through all array elements
    for i in range(1, n):
        # Last i elements are already in place
        for j in range(0, n - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next one
            if (a[j] > a[j + 1]):
                temp = a[j]
                a[j] = a[j + 1]
                # Driver code to test above code
                a[j + 1] = temp

numbers = [25, 14, 11, 33, 15, 16, 31, 22]
print("Unsorted Numbers:")
print(numbers)
time.sleep(2)
print(" ")
BubbleSort(numbers)
print("Sorted Numbers:")
print(numbers)