"""
HERE IS MOST POPULAR FUNCTIONS OF SORTING FOR PYTHON AND EXPLANATION FOR ALL
YOU CAN FREE USE IT ON YOUR PROJECT OR LEARNING HOW IT'S WORKS
"""

"""
THE FIRST SORTING PRINCIPLE: BUBBLE SORT

The principle of Bubble Sort consists in sequentially comparing pairs of adjacent elements in the list and exchanging 
their places if they are in the wrong order. 
This process is repeated for several iterations until the entire list is sorted.
The basic idea is that at each iteration the largest (or smallest) element "floats" to the end of the list, 
similar to how a bubble rises to the surface of water. 
This results in gradually sorting the elements in the correct order.
"""


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    #  this sort does not return a result, you need to use it directly on the list


"""
THE SECOND SORTING PRINCIPAL: INSERTION SORT
The principle of insertion sort (Insertion Sort) is to sequentially insert elements into the sorted part of the list. 
The algorithm starts with the first element and gradually goes through each subsequent element, 
inserting it into the corresponding position in the already sorted part of the list. This process is repeated until all 
elements have been sorted.
The basic idea is that on each iteration the algorithm takes the next element and compares it to all the elements in the
 sorted part of the list. It shifts larger elements to the right, making room for the current element to be inserted.
"""


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    #  this sort does not return a result, you need to use it directly on the list


"""
THE THIRD SORTING PRINCIPAL: SELECTION SORT
The principle of sorting by exchange (Selection Sort) consists in sequentially choosing the smallest (or largest) 
element from the unsorted part of the list and exchanging it with the first element in the unsorted part. This process 
is repeated for each subsequent element, decreasing the number of unsorted elements by one on each iteration.
The basic idea is that at each iteration the algorithm looks for the smallest (or largest) element in the unsorted part 
of the list and exchanges it with the first element in the unsorted part. This process continues until the entire list 
is sorted.
"""


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        #  this sort does not return a result, you need to use it directly on the list


"""
THE FOURTH SORTING PRINCIPAL: QUICK SORT
The principle of quick sort (Quick Sort) consists in recursively dividing the list into smaller sub lists based on the
selected reference element (pivot), similar to merge sort. All elements smaller than the pivot are placed before it,
and all elements greater than or equal to it are placed after it. The left and right parts of the list are then
recursively sorted around the pivot. This process is repeated until each sublist is sorted.
The basic idea is that the algorithm chooses a reference element (pivot), usually the middle element, and places it in 
the appropriate place, so that all elements smaller than it are placed before it, and all elements larger than it are 
placed after it. A recursive procedure is then called to sort the left and right parts of the list around the pivot. 
This process is repeated for each part until the entire list is sorted.
"""


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)
    # THIS SORT RETURN DATA, SO YOU NEED MAKE A NEW VARIABLE FOR RESULT
