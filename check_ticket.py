# 使用队列实现生产者-消费者
"""
模拟检票过程
排3队进行检票，一个队列一个线程
票有编号
检票时间有固定窗口，若时间到了通知队列关闭
"""
import queue
import threading
import time

eixtsingle = False


def queue_enter(threadname, queuelist):
    while not eixtsingle:
        queueLock.acquire()
        if not workQueue.empty():
            data = workQueue.get()
            queueLock.release()
            print("%s check ticket %s" % (threadname, data))
        else:
            queueLock.release()
        time.sleep(1)


class MyThread(threading.Thread):
    def __init__(self, threadname, queuelist):
        threading.Thread.__init__(self)
        self.threadname = threadname
        self.queuelist = queuelist

    def run(self):
        print("Starting queue %s" % self.threadname)
        queue_enter(self.threadname, self.queuelist)
        time.sleep(1)
        print("close  " + self.threadname)


if __name__ == "__main__":
    threadlist = ['list1', 'list2', 'list3']
    queueLock = threading.Lock()
    workQueue = queue.Queue()
    threads = []

    queueLock.acquire()
    for i in range(100001, 100020):
        workQueue.put(i)
    queueLock.release()

    print("start.....")
    for name in threadlist:
        thread = MyThread(name, workQueue)
        thread.start()
        threads.append(thread)
    while not workQueue.empty():
        pass
    eixtsingle = True
    for t in threads:
        t.join()
    print("stop enter....")
