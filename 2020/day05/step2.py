def countChar(c, s):
    count = 0
    for i in range(len(s)):
        if (s[i] == c):
            count = count + 1
    return count

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

result = 0
ids = []

for line in f:
    row = 0
    for i in range(7):
        if line[i] == "B":
            row = row + (2 ** (7 - (i + 1)))
        
    seat = 0
    for i in range(3):
        if line[i + 7] == "R":
            seat = seat + (2 ** (10 - (i + 8)))
    
    id = (row * 8) + seat
    ids.append(id)
    
    print(line.rstrip() + ": row " + str(row) + ", column: " + str(seat) + ", seat ID: " + str(id))
        
quickSort(ids, 0, len(ids) - 1)


for i in range(1, len(ids)):
    if ids[i] - ids[i - 1] == 2:
        print(ids[i] - 1)
        break

f.close()
