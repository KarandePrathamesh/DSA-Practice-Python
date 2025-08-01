#  w. a. p. to reverse word in string
#  e.g str = "Hello all Welcome"
# o/p =>   Welcome all Hello

def reverseString(str):
    arr=[]
    word=''
    # Read character
    for ch in str:
        if ch == ' ':
            arr.append(word)
            word = ' '
        else:
            word+=ch
        
    if word:
        arr.append(word)
    return " ".join(arr[::-1])

str = "Hello all Welcome"
print(reverseString(str))
