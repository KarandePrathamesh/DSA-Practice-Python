def exchangeSort(arr):
    size = len(arr)
    for i in range(size):
        for j in range(i+1, size):
            if(arr[i]>arr[j]):                   # if > sorts ascending , or < sorts descending order
                arr[i], arr[j] = arr[j], arr[i]

arr = [34,2,5,67,78,89,34,1]
exchangeSort(arr)
for i in range(len(arr)-1):
    print(arr[i],end=' ')