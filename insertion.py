import time

def insertion_sort(arr):
  for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and key < arr[j]:
      arr[j + 1] = arr[j]
      j -= 1
    arr[j + 1] = key

def main():
  arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
  print("Unsorted array: ", arr)
  start = time.time()
  insertion_sort(arr)
  end = time.time()
  print("Sorted array: ", arr)
  print("Time taken: ", end - start)

if __name__ == "__main__":
  main()