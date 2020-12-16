# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
 
 
def partition(arr, low, high):
    i = (low-1)         # index of smaller element
    pivot = arr[high]     # pivot
 
    for j in range(low, high):
 
        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
 
            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
 
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
 
# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index
 
# Function to do Quick sort
def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
 
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)
 
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
    
f = open("input.txt", "r")

numbers = []
for line in f:
    number = int(line.rstrip())
    numbers.append(number)

target = 167829540
for i in range(len(numbers)):
    total = 0
    j = i
    while j < len(numbers):
        total = total + numbers[j]
        if total >= target:
            break
        j = j + 1
    
    if total == target:
        sumNumbers = []
        for k in range(i, j):
            sumNumbers.append(numbers[k])
        quickSort(sumNumbers, 0, len(sumNumbers) - 1)
        print(sumNumbers[0] + sumNumbers[len(sumNumbers) - 1])
        break
            
f.close()
