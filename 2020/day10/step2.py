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

def validConnection(first, second):
    if second - first >= 1 and second - first <= 3:
        return True
    return False
    
combinations = {}
def countCombinations(numbers, i, paths):
    print("i: " + str(i) + ", Paths: " + str(paths))
    global combinations
    if i == len(numbers) - 1:
        return paths
        
    newPaths = -1
    totalPaths = 0
    if validConnection(numbers[i], numbers[i + 1]):
        if (i + 1) in combinations:
            totalPaths = combinations[i + 1]
        else:
            totalPaths = countCombinations(numbers, i + 1, paths)
        newPaths = newPaths + 1

    if i + 2 < len(numbers):
        if validConnection(numbers[i], numbers[i + 2]):
            newPaths = newPaths + 1
            if (i + 2) in combinations:
                totalPaths = totalPaths + combinations[i + 2]
            else:
                totalPaths = totalPaths + countCombinations(numbers, i + 2,  paths)
            
    if i + 3 < len(numbers):
        if validConnection(numbers[i], numbers[i + 3]):
            newPaths = newPaths + 1
            if (i + 3) in combinations:
                totalPaths = totalPaths + combinations[i + 3]
            else:
                totalPaths = totalPaths + countCombinations(numbers, i + 3,  paths)
            
    combinations[i] = totalPaths
    return totalPaths
    
f = open("input.txt", "r")

numbers = []
for line in f:
    number = int(line.rstrip())
    numbers.append(number)

numbers.append(0)
quickSort(numbers, 0, len(numbers) - 1)
result = countCombinations(numbers, 0, 1)
print(combinations)
print(result)

f.close()
