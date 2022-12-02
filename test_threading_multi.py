import threading
import time

balance = 0


def change_it(n):
    global balance
    balance += n
    time.sleep(2)
    balance -= n
    time.sleep(1)
    print('--------->{0};------{1}'.format(n,balance))

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