# find the longest pallindrom substring
# str = 'startraffic'
# subStr1='rtr'     3
# subStr2='artra'   5
# subStr2='ff'      2

def checkPallindrome(str,i,j):
    while(i<j):
        if str[i]!=str[j]:
            return False
        i+=1
        j+=1
        return True
    
def longestPallindrome(str):
    length = len(str)
    maxLen = 1
    start = 0
    for i in range(length):
        for j in range(i, length):
            if checkPallindrome(str,i,j):
                if(j-i+1)>maxLen:
                    start = i
                    maxLen = j-i+1
    return (str[start:start+maxLen])

# Driver code
str = 'startraffic'
print(longestPallindrome(str))
