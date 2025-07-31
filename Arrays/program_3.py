# Find out the first occurance of substring in a string
# str = "Hello world! Hello all!"
# subStr = "Hello"
# print(str.index(subStr))

# Find out the all occurance of substring in a string
str = "Hello world! Hello all!"
subStr = "Hello"
position=[]
s=0
while True:
    i = str.find(subStr,s)
    if i!=-1:
        position.append(i)
        s=s+len(subStr)
    else:
        break
print(position)