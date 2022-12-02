# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import math

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def lisan_qushi(list_a):


    jicha_a = max(list_a) - min(list_a)

    pingjuncha_a = sum( [abs(i - avg(list_a)) for i in  list_a] )/ len(list_a)

    biaozhuncha_a = math.sqrt(sum( math.pow(i - avg(list_a),2 ) for i in list_a  ) / len(list_a))
    return jicha_a, pingjuncha_a, biaozhuncha_a
def avg(list):
    return sum(list) / len(list)


def extend_list(val, l = []):
    l.append(val)
    return l

class Cat(object):
    def __init__(self):
        print("对象产生",id(self))
    def __del__(self):
        print("对象删除", id(self))
def f0():
    while True:
        c1 = Cat()


def f1():
    l = []
    while True:
        c1 = Cat()
        l.append(c1)
        print(len(l))




if __name__ == '__main__':
    f1()
