# 使用threading.condition实现生产者-消费者
"""
condition条件对象提供如下方法：
1.threading.Condition()
2.acquire(*args) 获取锁
3.release()释放锁
4.wait([timeout]) 等待
5.notify(n=1) / notifyAll() 唤醒
"""

"""
实例：
一件产品。投放到市场上，市场需求可以看作一个箱子box，有一个容量限度
当小于box大小，生产者可以生产，否则等待消费者消费，生产者有生产效率，使用speed表示
当产品大于0，才可进行消费，否则就等待生产者生产
"""

import threading
import time
from decimal import Decimal


condition = threading.Condition()
num = 0
box_size = 15


class GoodsProduce(threading.Thread):
    def __init__(self, companyName, produceSpeed, info):
        super(GoodsProduce, self).__init__()
        self.companyName = companyName
        self.produceSpeed = Decimal(2 / produceSpeed).quantize(Decimal("0.00"))
        self.info = info

    def run(self):
        global num
        while True:
            if condition.acquire():
                if num < box_size:
                    time.sleep(self.produceSpeed)
                    num += 1
                    print("GoodsProduce : %s create one , now box have :%d" % (self.companyName, num))
                    condition.notify()
                    condition.release()
            else:
                print("NOTE: BOX is full , size %d ,filled %d" % (box_size, num))
                condition.wait()

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
        global num
        while True:
            if condition.acquire():
                if num >= 1:
                    num -= 1
                    print("GoodsConsumer : %s get one , now box have :%d" % (self.cname, num))
                    condition.notify()
                    condition.release()
            else:
                time.sleep(1)
                print("NOTE: BOX is null , please wait ...  size %d ,fillin 0" % box_size)
                condition.wait()
            time.sleep(1)

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

