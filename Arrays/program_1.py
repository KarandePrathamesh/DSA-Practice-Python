# Input Sorted Array - w.a.fun that return true if there exist  pair of numbers that sum to target

# Test Case 1
# arr = [5,9,2,1,0,7,15]
# target = 12

# Test Case 2
# arr = [0,1,2,5,7,9,15]
# target = 12


# Brute force
# def targetSum(arr,target):
#     for i in range(0,len(arr)-1):
#         for j in range(i+1,len(arr)):
#             if arr[i]+arr[j]==target:
#                 print(arr[i])
#                 print(arr[j])
#                 return True


def targetSum(arr,target):
    left = 0
    right = len(arr)-1
    while(left<right):
        sum = arr[left]+arr[right]
        if(sum>target):
            right = right-1
        elif(sum<target):
            left=left+1
        else:
            print(arr[left])
            print(arr[right])
            return True
    return False
        
                  
arr = [0,1,2,5,7,9,15]
target = 12
result = targetSum(arr,target)
print(result)
