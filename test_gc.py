import gc
import sys
import objgraph


print(gc.get_threshold())

class Person(object):
    pass

class Cat(object):
    pass

p = Person()
c = Cat()
p.name = 'susan'
p.pet = c

c.master = p
print(sys.getrefcount(p))
print(sys.getrefcount(c))
# del p
# del c

# 手动执行垃圾回收
gc.collect()
print(objgraph.count('Person'))
print(objgraph.count('Cat'))