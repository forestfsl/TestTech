#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:songlin
@time: 2022/11/19 22:15
"""
import _thread
import logging
import threading
from time import sleep,ctime

logging.basicConfig(level=logging.INFO)

"""
INFO:root:start all atSat Nov 19 22:20:52 2022
INFO:root:start loop0 atSat Nov 19 22:20:52 2022
INFO:root:end loop0 atSat Nov 19 22:20:56 2022
INFO:root:start loop1 atSat Nov 19 22:20:56 2022
INFO:root:end loop1 atSat Nov 19 22:20:58 2022
INFO:root:end all atSat Nov 19 22:20:58 2022
"""
# def loop0():
#     logging.info("start loop0 at" + ctime())
#     sleep(4)
#     logging.info("end loop0 at" + ctime())
#
# def loop1():
#     logging.info("start loop1 at" + ctime())
#     sleep(2)
#     logging.info("end loop1 at" + ctime())
#
# def main():
#     logging.info("start all at" + ctime())
#     loop0()
#     loop1()
#     logging.info("end all at" + ctime())
#
# if __name__ == '__main__':
#     main()

"""
INFO:root:start all atSat Nov 19 22:22:54 2022
INFO:root:start loop0 atSat Nov 19 22:22:54 2022
INFO:root:start loop1 atSat Nov 19 22:22:54 2022
INFO:root:end loop1 atSat Nov 19 22:22:56 2022
INFO:root:end loop0 atSat Nov 19 22:22:58 2022
INFO:root:end all atSat Nov 19 22:23:00 2022
"""
# def loop0():
#     logging.info("start loop0 at" + ctime())
#     sleep(4)
#     logging.info("end loop0 at" + ctime())
#
# def loop1():
#     logging.info("start loop1 at" + ctime())
#     sleep(2)
#     logging.info("end loop1 at" + ctime())
#
# def main():
#     logging.info("start all at" + ctime())
#     _thread.start_new_thread(loop0,())
#     _thread.start_new_thread(loop1, ())
#     #为什么加sleep(6) 这里有个不成文的规定，当主线程退出之后，所有线程都跟着退出
#     sleep(6)
#     logging.info("end all at" + ctime())
#
# if __name__ == '__main__':
#     main()


"""
INFO:root:start all atSat Nov 19 22:45:39 2022
INFO:root:start loop:0atSat Nov 19 22:45:39 2022
INFO:root:start loop:1atSat Nov 19 22:45:39 2022
INFO:root:end loop:0atSat Nov 19 22:45:41 2022
INFO:root:end loop:1atSat Nov 19 22:45:43 2022
INFO:root:end all atSat Nov 19 22:45:43 2022

"""

"""
线程是没有先后顺序的
INFO:root:start all atSat Nov 19 22:51:55 2022
INFO:root:start loop:0atSat Nov 19 22:51:55 2022
INFO:root:start loop:1atSat Nov 19 22:51:55 2022
INFO:root:end loop:0atSat Nov 19 22:51:57 2022
INFO:root:end loop:1atSat Nov 19 22:51:59 2022
INFO:root:end all atSat Nov 19 22:51:59 2022
"""
# loops = [2,4]
# def loop(nloop,nsec):
#     logging.info("start loop:" + str(nloop) + "at" + ctime())
#     sleep(nsec)
#     logging.info("end loop:" + str(nloop) + "at" + ctime())
#
# def main():
#     logging.info("start all at" + ctime())
#     threads = []
#     nloops = range(len(loops))
#     for i in nloops:
#         t = threading.Thread(target=loop, args=(i,loops[i]))
#         threads.append(t)
#     for i in nloops:
#         threads[i].start()
#     for i in nloops:
#         threads[i].join()
#     logging.info("end all at" + ctime())

"""
INFO:root:start all atSat Nov 19 22:56:41 2022
INFO:root:start loop:1atSat Nov 19 22:56:41 2022
INFO:root:start loop:0atSat Nov 19 22:56:41 2022
INFO:root:end loop:0atSat Nov 19 22:56:43 2022
INFO:root:end loop:1atSat Nov 19 22:56:45 2022
INFO:root:end all atSat Nov 19 22:56:45 2022

"""
class MyThread(threading.Thread):
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name
    def run(self) -> None:
        self.func(*self.args)

loops = [2,4]
def loop(nloop,nsec):
    logging.info("start loop:" + str(nloop) + "at" + ctime())
    sleep(nsec)
    logging.info("end loop:" + str(nloop) + "at" + ctime())

def main():
    logging.info("start all at" + ctime())
    threads = []
    nloops = range(len(loops))
    for i in nloops:
        t = MyThread(loop,(i,loops[i]),loop.__name__)
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()
    logging.info("end all at" + ctime())


if __name__ == '__main__':
    main()