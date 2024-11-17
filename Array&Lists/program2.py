l1 = [1, 10, 20, 30, 40]
l2 = [30, 40, 45, 92]

l1.append(l2)
print(l1)

l3 = l1.copy()
print(l3) 

print(l1.count(30))
print(l2.index(30))
print(l2.pop(1))

l2.extend(l1)
print(l2)

l2.insert(1,46)
print(l2)

l1.remove(20)
print(l1)

l1.reverse()
print(l1)
