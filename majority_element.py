def majority_element(arr):
  freq = {}
  n = len(arr)

  for x in arr:
    freq[x] = freq.get(x, 0) + 1
    if freq[x] > n // 2:
      return x
  return -1
