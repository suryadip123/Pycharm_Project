l1 = [1,2,3]
l2 = [1,5,6]

l = list(set(l1).union(l2))
print(l)

print(list(set(l1) | set(l2)))