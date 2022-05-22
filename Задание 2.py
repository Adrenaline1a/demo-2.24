import math
from threading import Lock, Thread
from queue import Queue


def func2():
    while not q.empty():
        s = q.get()
        y = math.cos(s)
        print(f'y = {y}')


def func1():
    lock.acquire()
    x = 0.3
    EPS = 1e-07
    S, n = 0, 1
    while True:
        S1 = ((-1)**(n-1)*x**(2*(n-1)))/(math.factorial(2*(n-1)))
        n += 1
        S2 = ((-1)**n*x**(2*n))/(math.factorial(2*n))
        if abs(S2 - S1) < EPS:
            break
        S += S2
        print(f"S = {S}")
        q.put(S)
    lock.release()


if __name__ == "__main__":
    q = Queue()
    lock = Lock()
    th1 = Thread(target=func1).start()
    th2 = Thread(target=func2).start()
