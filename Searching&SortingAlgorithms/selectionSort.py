def selectionSort(arr):
    size = len(arr)-1
    for i in range(size):
        min_index = i
        for j in range(i+1, size):
            if(arr[j]<arr[min_index]):
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

arr = [34,2,5,67,78,89,34,1]
selectionSort(arr)
for i in range(len(arr)-1):
    print(arr[i],end=' ')