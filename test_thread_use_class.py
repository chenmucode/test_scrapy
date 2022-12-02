import time
from threading import Thread
import threading

class LoopThread(Thread):
    n = 0
    def run(self) -> None:
        now_thread = threading.current_thread()
        print("loop_thread:", now_thread.name)
        n = 0
        while n < 5:
            print(n)
            now_thread = threading.current_thread()
            print("loop_thread:", now_thread.name)
            time.sleep(1)
            n += 1
if __name__ == '__main__':
    now_thread = threading.current_thread()
    print("loop_thread:", now_thread.name)
    t = LoopThread(name='loop_thread_oop')
    t.start()
    t.join()
