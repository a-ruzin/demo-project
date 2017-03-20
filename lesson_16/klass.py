import os
import queue
import random
import threading
import timeit
from threading import Thread, Lock, RLock, Semaphore, BoundedSemaphore
import time

# ================ subprocess
# import subprocess
#
# result = subprocess.call(["python", "print.py"])
# # result = subprocess.call("cat klass.py", shell=True)
# # print(result)
#
#
# # with open('klass.py', 'rb') as f, open('klass2.py', 'wb') as f2:
# with open('../../analytics.tgz', 'rb') as f:
#     proc = subprocess.Popen("cat", stdin=f, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
#     print('my pid: {}'.format(os.getpid()))
#     print('pid: {}'.format(proc.pid))
#     try:
#         outs, errs = proc.communicate(timeout=15)
#         print(outs[:10], len(outs))
#     except subprocess.TimeoutExpired:
#         proc.kill()
#         outs, errs = proc.communicate()



# ====================== последовательное vs параллельное
# def count(n):
#     while n > 0:
#         n -= 1
#
# N = 10000000
#
# start_time = timeit.default_timer()
# count(N)
# count(N)
# elapsed = timeit.default_timer() - start_time
# print("Method 1: {}", elapsed)
#
#
# start_time = timeit.default_timer()
# t1 = Thread(target=count, args=(N,))
# t1.start()
# t2 = Thread(target=count, args=(N,))
# t2.start()
# t1.join(); t2.join()
# elapsed = timeit.default_timer() - start_time
# print("Method 2: {}", elapsed)


# ========================= Lock vs RLock
# a = Semaphore(1)
# print("before first acquire")
# a.acquire()
# print("before second acquire")
# a.acquire()
# print("before first release")
# a.release()
# print("before second release")
# a.release()
# print("the end")


# ======================= threading.local()
# common = 1
#
# def x():
#     time.sleep(1)
#     global common
#     common = threading.local()
#     common.a = 10
#     print('{} changed to {}'.format(threading.current_thread().name, common.a))
#
# def y():
#     print("{} - {}".format(threading.current_thread().name, common))
#     threading.current_thread().name = 'Ho-ho-ho'
#     time.sleep(2)
#     print("{} - {}".format(threading.current_thread().name, common))
#
# t1 = Thread(target=x)
# t2 = Thread(target=y)
#
# t1.start()
# t2.start()
#
# print("t1 name is {}".format(t1.name))
#
# t1.join()
# t2.join()


# ====================== Queue & threading ===
#
# def worker():
#     while True:
#         item = q.get()
#         if item is None:
#             break
#         print(threading.current_thread().name, item)
#         time.sleep(random.random())
#         q.task_done()
#
# q = queue.Queue(maxsize=5)
# threads = []
# for i in range(5):
#     t = threading.Thread(target=worker)
#     t.start()
#     threads.append(t)
#
# for item in range(100):
#     q.put(item)
#
# # block until all tasks are done
# q.join()
#
# # stop workers
# for i in range(5):
#     q.put(None)
# for t in threads:
#     t.join()




# ============================ multiprocessing
import multiprocessing as mp

def foo(q):
    q.put('hello')

if __name__ == '__main__':
    mp.set_start_method('spawn')
    q = mp.Queue()
    p = mp.Process(target=foo, args=(q,))
    p.start()
    print(q.get())
    p.join()

# ============================ multiprocessing
# from multiprocessing import Pool
# import time
#
# def f(x):
#     return x*x
#
# with Pool(processes=4) as pool:
#     result = pool.apply_async(f, (10,))
#     print(result.get(timeout=1))
#
#     print(pool.map(f, range(10)))
#
#     it = pool.imap(f, range(10))
#     print(next(it))
#     print(next(it))
#     print(it.next(timeout=1))
#
#     result = pool.apply_async(time.sleep, (10,))
#     print(result.get(timeout=1))        # raises multiprocessing.TimeoutError


# import time, random
# from multiprocessing import Process, Pipe, current_process
# from multiprocessing.connection import wait
#
# import multiprocessing
#
#
# def foo(w):
#     for i in range(10):
#         w.send((i, current_process().name))
#     w.close()
#     time.sleep(1)
#     print(current_process().name, 'closed')
#
# if __name__ == '__main__':
#     readers = []
#
#     for i in range(4):
#         r, w = Pipe(duplex=False)
#         readers.append(r)
#         p = Process(target=foo, args=(w,))
#         p.start()
#         w.close()
#
#     while readers:
#         for r in wait(readers):
#             try:
#                 msg = r.recv()
#             except EOFError:
#                 print('r is closed', r)
#                 readers.remove(r)
#             else:
#                 print(msg)

# ================== Pool
# import multiprocessing
#
#
# def cube(x):
#     res = x*x*x
#     time.sleep(.1)
#     print(os.getpid(), multiprocessing.current_process().name, x, res)
#     return res
#
# def callback(arg):
#     print(arg, end=", ")
#
# start = timeit.default_timer()
# pool = multiprocessing.Pool(processes=4)
# # results = [pool.apply(cube, args=(x,)) for x in range(1, 100)]
# # print(results)
# results = [pool.apply_async(cube, args=(x,), callback=callback) for x in range(1, 100)]
# # print([r.get() for r in results])
# print('total: ', timeit.default_timer()-start)