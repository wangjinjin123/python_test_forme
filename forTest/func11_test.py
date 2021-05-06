"""
python多线程
进程：
执行中的程序；
拥有独立的地址空间、内存、数据栈等
操作系统管理
派生（fork/spawn）新进程
进程间通信（IPC）方式共享信息

线程：
同进程下执行，共享相同的上下文
线程间的信息共享和通信更加容易
多线程并发执行  并发即轮询执行而不是同一时刻同时进行
需要同步原语？


python与线程
python是一个解释器
解释器主循环
主循环在哄只有一个控制线程在执行
使用全局解释器锁（GIL）---同步原语的一个技术


GIL保证一个线程
设置GIL
切换进一个线程去运行
执行下面的操作之一






两种线程管理
_thread:提供了基本的线程和锁
threading:提供了更高级别、功能更全面的线程管理
     支持同步机制
    支持守护线程
"""
import _thread
import logging
from time import sleep, ctime

"""
_thread模块
thread模块的函数：
start_new_thread(function,args,kwargs=None):派生一个新的线程，使用给定的args和可选的kyargs来执行function
allocate_lock():分配LockType锁对象
exit() 给线程退出指令

LockType锁对象的方法
acquire(wait = None) 尝试获取锁对象
locked() 如果获取了锁对象，则返回True 否则返回false
release() 释放锁
"""
#日志输出
# logging.basicConfig(level=logging.INFO)
# def loop0():
#     logging.info("start loop0 at" + ctime())
#     sleep(4)
#     logging.info("end loop0 at" + ctime())
#
# def loop1():
#     logging.info("start loop1 at" + ctime())
#     sleep(2)
#     logging.info("end loop0 at" + ctime())
#
# def main():
#     logging.info("start all at" + ctime)
#     loop0()
#     loop1()
#     logging.info("end all at" + ctime)
#
# if __name__ == '__main__':
#     main()


#使用线程优化
# logging.basicConfig(level=logging.INFO)
# def loop0():
#     logging.info("start loop0 at" + ctime())
#     sleep(4)
#     logging.info("end loop0 at" + ctime())
#
# def loop1():
#     logging.info("start loop1 at" + ctime())
#     sleep(2)
#     logging.info("end loop0 at" + ctime())
#
# def main():
#     logging.info("start all at" + ctime)
#     _thread.start_new_thread(loop0())
#     _thread.start_new_thread(loop1()) #主线程退出后所有子线程均被杀掉
#     sleep(6)
#     logging.info("end all at" + ctime)
#
# if __name__ == '__main__':
#     main()

#监视子进程是否完成不完成就无限等待---锁

logging.basicConfig(level=logging.INFO)
def loop0():
    logging.info("start loop0 at" + ctime())
    sleep(4)
    logging.info("end loop0 at" + ctime())

def loop1():
    logging.info("start loop1 at" + ctime())
    sleep(2)
    logging.info("end loop0 at" + ctime())

def main():
    logging.info("start all at" + ctime)
    _thread.start_new_thread(loop0())
    _thread.start_new_thread(loop1()) #主线程退出后所有子线程均被杀掉
    sleep(6)
    logging.info("end all at" + ctime)

if __name__ == '__main__':
    main()


