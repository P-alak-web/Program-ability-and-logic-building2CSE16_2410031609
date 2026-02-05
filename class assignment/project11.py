import heapq
def  kthsmallestelement(arr,k):
  # min heap of array
  heapq.heapify(arr)
  print(f"min heap array :{arr}")

 #poppint k-1 element from heap
  for _ in range(k-1):
    heapq.heappop(arr)
 #returning kth smallest element
  return heapq.heappop(arr)

arr = [100,17,36,25,19,7,3,2,1]
k = 4
print(f"normal array:{arr}")
print(f"{k}th smallest eleement:{kthsmallestelement(arr,k) }")
