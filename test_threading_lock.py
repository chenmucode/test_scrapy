import threading
import time
# 获得一把锁
my_lock = threading.Lock()
# Rlock可以重复锁，但锁n次就要解锁n次 
your_lock = threading.RLock()

balance = 0

def change_it(n):
    global balance
    try:
        # 添加锁
        my_lock.acquire()
        # 资源已经被锁住了，不能重复锁定，再锁会产生阻塞 - 死锁
        # my_lock.acquire()
        balance += n
        time.sleep(2)
        balance -= n
        time.sleep(1)
        print('--------->{0};------{1}'.format(n,balance))
    finally:
        # 释放锁
        my_lock.release()

class ChangeBalanceThread(threading.Thread):
    def __init__(self,num, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.num = num

    def run(self) -> None:
        for i in range(10000000):
            change_it(self.num)

if __name__ == '__main__':
    t1 = ChangeBalanceThread(5)
    t2 = ChangeBalanceThread(8)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("the last:{0}".format(balance))