import sys


del l2
print(sys.getrefcount(l))
i = 32132131
print(sys.getrefcount(i))
a = i
print(sys.getrefcount(i))


if __name__ == '__main__':
    print(1)好的后期后
