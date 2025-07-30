def binarySearch(arr, low, high, key):
    while low<=high:
        mid = (low+high)//2
        if(key<arr[mid]):
            high = mid-1
        elif(key>arr[mid]):
            low = mid+1
        else:
            return mid

arr = [1,54,45,23,67,33]
key = 67
result = binarySearch(arr,0,len(arr)-1,key)
if(result!=-1):
 print('element found at',result)
else:
 print('element not found')

