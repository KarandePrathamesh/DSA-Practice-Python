def bubbleSort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if(arr[j]>arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [34,2,5,67,78,89,34,1]
bubbleSort(arr)
for i in range(len(arr)-1):
    print(arr[i],end=' ')