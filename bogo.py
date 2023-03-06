import random
import time

def bogosort(arr):
  while not is_sorted(arr):
    random.shuffle(arr)
  return arr
  
def is_sorted(arr):
  for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
      return False
  return True
  
def main():
  arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
  print("Unsorted array: ", arr)
  start = time.time()
  arr = bogosort(arr)
  end = time.time()
  print("Sorted array: ", arr)
  print("Time taken: ", end - start)
  
if __name__ == "__main__":
  main()