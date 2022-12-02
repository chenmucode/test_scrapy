import sys

l = []
l2 = l
l3 = l
l5 = l3
print(sys.getrefcount(l))

del l2
print(sys.getrefcount(l))
i = 2
print(sys.getrefcount(i))
a = i
print(sys.getrefcount(i))
