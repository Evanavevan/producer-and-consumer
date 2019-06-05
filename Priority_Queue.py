# 优先对列
import queue
import random

queuelist = queue.PriorityQueue()

for i in range(5):
    if not queuelist.full():
        x = random.randint(1, 20)
        y = random.randint(1, 20)
        print(y, x)
        queuelist.put([y, "th-%d" % x])
while not queuelist.empty():
    print("put list : %s ,now queue size is %s " % (queuelist.get(), queuelist.qsize()))