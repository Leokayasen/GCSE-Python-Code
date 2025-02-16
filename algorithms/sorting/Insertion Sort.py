# Function to run insertionSort
import time

def insertionSort(array):
    # We start from 1 since the first element is trivially sorted
    for index in range(1, len(array)):
        currentValue = array[index]
        currentPosition = index

        # As long as we haven't reached the beginning and there is an element in our sorted array
        # which is larger than the one we're trying to insert

        # Move that element to the right
        while currentPosition > 0 and array[currentPosition - 1] > currentValue:  # <
            array[currentPosition] = array[currentPosition - 1]  # <
            currentPosition = currentPosition - 1

        # We have either reached the beginning of the array
        # or we have found an element of the sorted array that is smaller than the element
        # that we're trying to insert at Index currentPosition -1

        # Either way, we must insert the element at currentPosition
        array[currentPosition] = currentValue


array = [4, 22, 41, 27, 30, 36, 16, 42, 37, 14, 39, 3, 6, 34, 9, 21, 2, 29, 47]
print("Unsorted Array:")
print(array)
time.sleep(2)
print(" ")
insertionSort(array)
print("Sorted array: ")
print(str(array))