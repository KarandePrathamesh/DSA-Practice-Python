from array import *
a1 = array('i',[35,45,46,92])
print(type(a1))
print(a1)

for x in a1:
    print(x)

for i in range(4):
    print(a1[i],end=' ')

i=0
while (i<len(a1)):
    print(a1[i])
    i+=1

#Array methods
a1.append(20)
print(a1)

print(a1.count(20))
print(a1.count(92))

print(a1.index(92))  #returns index of element

a1.pop()  #last element pop hoga
print(a1)
a1.pop(0)  #indexing gheun delete krt
print(a1)

a1.remove(46)
print(a1)

a1.append(20)
a1.append(30)
a1.append(40)
a1.append(50)
print(a1)


a1.reverse()  #reversing array elements
print(a1)

print(a1.tolist()) #converting array into list
# print(a1.tofile())