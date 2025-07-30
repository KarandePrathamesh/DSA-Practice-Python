def binarySearch(arr, low, high, key):
    mid = (low+high)//2
    if(key>arr[mid]):
        low = mid + 1
        return binarySearch(arr, low, high, key)
    elif(key<arr[mid]):
        high = mid - 1
        return binarySearch(arr, low, high, key)
    else:
        return mid


arr = [1,3,5,34,42,56,78,89,90]
key = 56
result = binarySearch(arr, 0, len(arr)-1, key)
if(result!=-1):
    print('element found at index',result)
else:
    print('element not found at any index')