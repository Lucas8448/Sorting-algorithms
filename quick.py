import time

def quick_sort(arr, low, high):
  if low < high:
    pi = partition(arr, low, high)
    quick_sort(arr, low, pi - 1)
    quick_sort(arr, pi + 1, high)
    
def partition(arr, low, high):
  i = low - 1
  pivot = arr[high]
  for j in range(low, high):
    if arr[j] < pivot:
      i += 1
      arr[i], arr[j] = arr[j], arr[i]
  arr[i + 1], arr[high] = arr[high], arr[i + 1]
  return i + 1
  
def main():
  arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
  print("Unsorted array: ", arr)
  start = time.time()
  quick_sort(arr, 0, len(arr) - 1)
  end = time.time()
  print("Sorted array: ", arr)
  print("Time taken: ", end - start)
  
if __name__ == "__main__":
  main()