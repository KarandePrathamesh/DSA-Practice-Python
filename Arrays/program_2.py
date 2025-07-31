# Remove duplicates from array
def removeDuplicate(arr):
    for i in arr:
       if i not in result:
           result.append(i) 

arr = [5,3,2,5,4,9,3]
result = []
removeDuplicate(arr)
print(arr)
print(result)