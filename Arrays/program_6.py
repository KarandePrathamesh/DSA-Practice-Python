# wap to print sum of subarray which gives maximum sum
# e.g arr = [-7,2,3,-5,9,-1,0,4]

def maxSumSubArray(arr):
    maxSum = arr[0]
    for i in range(len(arr)):
        currentSum = 0
        for j in range(i+1, len(arr)):
            currentSum += arr[j]
            maxSum = max(maxSum, currentSum)
    return maxSum


# 9+4=12
# if all postivite numbers in array then maxSum will be the sum of all elements in array
arr = [-7,2,3,-5,9,-1,0,4]
print(maxSumSubArray(arr))