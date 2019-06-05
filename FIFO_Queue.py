# FIFO队列先进先出
import queue

queuelist = queue.Queue()

for i in range(5):
    if not queuelist.full():
        queuelist.put(i)
        print("put list : %s ,now queue size is %s " % (i, queuelist.qsize()))
while not queuelist.empty():
    print("put list : %s ,now queue size is %s " % (queuelist.get(), queuelist.qsize()))