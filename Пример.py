#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from threading import Condition, Thread
from queue import Queue
from time import sleep


cv = Condition()
q = Queue()


def order_processor(name):
    while True:
        with cv:
            while q.empty():
                cv.wait()
            try:
                order = q.get_nowait()
                print(order.get("День"), order.get("Зарплата") - order.get("Вычеты за нарушения"))
                break
            except:
                pass
            sleep(0.1)
if __name__ == "__main__":
    Thread(target=order_processor, args=("thread 1",)).start()
    Thread(target=order_processor, args=("thread 2",)).start()
    Thread(target=order_processor, args=("thread 3",)).start()
    for i in range(30):
        q.put({
            "День": i,
            "Зарплата": 0,
            "Вычеты за нарушения": 0,
        })

    with cv:
        cv.notify_all()
