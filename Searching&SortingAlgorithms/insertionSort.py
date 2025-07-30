def insertionSort(arr):
    size = len(arr)
    for i in range(1, size):
        key = arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1]=key

arr = [34,2,5,67,78,89,34,1]
insertionSort(arr)
for i in range(len(arr)):
    print(arr[i],end=' ')