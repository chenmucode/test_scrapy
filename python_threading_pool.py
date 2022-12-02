import threading
import time
from concurrent.futures import ThreadPoolExecutor
from multiprocessing.dummy import Pool
import requests


def run(n):
    """线程要做的事"""
    time.sleep(1)
    print(threading.currentThread().name, n)

def main():
    """使用传统方法来做任务"""
    t1 = time.time()
    for n in range(5):
        run(n)
    print(time.time() - t1)

def main_use_thread():
    """使用线程优化任务"""
    t1 = time.time()
    # 资源有限，最多一次只能跑10个线程
    ls = []
    for count in range(10):
        for i in range(10):
            t = threading.Thread(target=run,args=(i,))
            ls.append(t)
            t.start()
        for l in ls:
            l.join()
    print(time.time() - t1)

def main_use_pool():
    """使用线程池来优化"""
    t1 = time.time()
    n_list = range(100)
    pool = Pool(10)
    pool.map(run, n_list)
    pool.close()
    pool.join()
    print(time.time() - t1)

def main_use_executor():
    t1 = time.time()
    n_list = range(100)
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(run,n_list)
    print(time.time() - t1)





if __name__ == '__main__':
    main_use_executor()
