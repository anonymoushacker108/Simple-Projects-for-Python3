
import random

def bubble_sort(arr, comparison_function):
    n = len(arr)
    for i in range(n):
        swapped = False
        for idx in range(0, n - i - 1):
            # USE the comparison function (don't use > on the dicts!)
            if comparison_function(arr[idx], arr[idx + 1]):
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
                swapped = True
        if not swapped:
            break
    return arr  # safe to return

def quicksort(list, start, end):
  if start >= end:
    return
  pivot_idx = random.randrange(start, end + 1)
  pivot_element = list[pivot_idx]
  list[end], list[pivot_idx] = list[pivot_idx], list[end]
  less_than_pointer = start
  for i in range(start, end):
    if pivot_element > list[i]:
      list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
      less_than_pointer += 1
  list[end], list[less_than_pointer] = list[less_than_pointer], list[end]
  quicksort(list, start, less_than_pointer - 1)
  quicksort(list, less_than_pointer + 1, end)
  def bubble_sort(arr, comparison_function):
    n = len(arr)
    for i in range(n):
        for idx in range(0, n - i - 1):
            # Use the provided comparison function
            if comparison_function(arr[idx], arr[idx + 1]):
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
    return arr

def comparison_function(a, b):
    return a > b  # True if first is greater than second
def greater_than(a, b):
    return a > b

# Test
nums = [5, 2, 9, 1, 5, 6]
sorted_nums = bubble_sort(nums, comparison_function)
print(sorted_nums)  # [1, 2, 5, 5, 6, 9]