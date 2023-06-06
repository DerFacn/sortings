from __init__ import *

example = [12, 31, 49, 33, 5, 80, 21]
print(f"Example list: {example}. \n")
bubble_sort(example)
print(f"Bubble sort: {example}.")

example = [12, 31, 49, 33, 5, 80, 21]
insertion_sort(example)
print(f"Insertion sort: {example}")

example = [12, 31, 49, 33, 5, 80, 21]
selection_sort(example)
print(f"Selection sort: {example}")

example = [12, 31, 49, 33, 5, 80, 21]
result = quick_sort(example)
print(f"Quick sort: {result}")
