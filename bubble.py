import time

def bubble_sort(arr):
  n = len(arr)
  for i in range(n):
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1] :
        arr[j], arr[j+1] = arr[j+1], arr[j]

def main():
  arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
  print("Unsorted array: ", arr)
  start = time.time()
  bubble_sort(arr)
  end = time.time()
  print("Sorted array: ", arr)
  print("Time taken: ", end - start)
  
if __name__ == "__main__":
  main()