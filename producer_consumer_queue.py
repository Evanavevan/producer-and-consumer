# 使用队列实现生产者-消费者
import threading
import queue
import time
import random
from decimal import Decimal

box = 15
queuelist = queue.Queue(box)

class GoodsProduce(threading.Thread):
    def __init__(self, companyName, produceSpeed, info):
        super(GoodsProduce, self).__init__()
        self.companyName = companyName
        self.produceSpeed = Decimal(2 / produceSpeed).quantize(Decimal("0.00"))
        self.info = info

    def run(self):
        while True:
            if not queuelist.full():
                time.sleep(self.produceSpeed)
                s = "goods-%d" % random.randint(1, 100)
                queuelist.put(s)
                print("GoodsProduce : %s create %s , now box have :%d" % (self.companyName, s, queuelist.qsize()))
            else:
                print("NOTE: BOX is full , size %d ,filled %d" % (box, box))
                time.sleep(1)

    def show(self):
        print("companyName -- %s ,produceSpeed -- %s, infomation -- %s" % (self.companyName, self.produceSpeed,
                                                                           self.info))


class GoodsConsume(threading.Thread):
    def __init__(self, cname, area, info):
        super(GoodsConsume, self).__init__()
        self.cname = cname
        self.area = area
        self.info = info

    def run(self):
        while True:
            if not queuelist.empty():
                gname = queuelist.get()
                print("GoodsConsumer : %s get %s , now box have :%d" % (self.cname, gname, queuelist.qsize()))
            else:
                time.sleep(1)
                print("NOTE: BOX is null , please wait ...  size %d ,fillin 0" % box)
            time.sleep(2)

    def show(self):
        print("GoodsConsume %s area -- %s ,infomation -- %s" % (self.cname, self.area, self.info))


if __name__ == "__main__":
    for server_num in range(0, 2):
        server = GoodsProduce("Prd-%d" % server_num, server_num + 1, "this is %d prd company" % server_num)
        server.start()
        server.show()

    for customer_num in range(0, 5):
        customer = GoodsConsume("cus-%d" % customer_num, "area-%d" % customer_num, "this is %d customer" % customer_num)
        customer.start()
        customer.show()
