import random
from threading import Lock, Thread
from queue import Queue


"""
Сдача сесии:
В лице производителя - список преподавателей, дающие задания студенту;
В лице потребителя - студент, сдающий соответсвующие работы преподавателям.
"""

def peresdacha():
    ls = []
    while True:
        s = qe.get()
        r = random.randint(2,5)
        print(f"Студент пересдал задание с id: {s[1]} преподавателю {s[0]} с оценкой {r}")
        ls.append(
            {
                "id": s[1],
                "Преподаватель": s[0],
                "Оценка": r
            }
        )
        if qe.empty():
            for i in ls:
                if i["Оценка"] == 2:
                    print(f"Студент не пересдал задание с id: {i['id']}, в связи с этим он отчислен")
            break


def consumer():
    lst = []
    while True:
        s = q.get()
        r = random.randint(2,5)
        print(f"Студент сдал задание с id: {s[1]} преподавателю {s[0]} с оценкой {r}")
        lst.append(
            {
                "id": s[1],
                "Преподаватель": s[0],
                "Оценка": r
            }
        )
        if q.empty():
            for i in lst:
                if i["Оценка"] == 2:
                    print(f"Студент не сдал задание с id: {i['id']} и отправляется на пересдачу")
                    qe.put([i["Преподаватель"], i["id"]])
            break


def producer(lst):
    lock.acquire()
    lst = lst
    for i in range(10):
        idx = random.randint(0, 4)
        exp = random.randint(1, 1000)
        #print(f'Преподаватель {lst[idx]} дал задание с id: {exp}')
        q.put([lst[idx], exp])
    lock.release()


if __name__ == "__main__":
    lst = ['Воронкин Р.А.', 'Говорова С.В.', 'Гайчук Д.В.', 'Мочалов В.П.', 'Баженов А.В.']
    lock = Lock()
    q = Queue()
    qe = Queue()
    th1 = Thread(target=producer(lst)).start()
    th2 = Thread(target=consumer).start()
    th3 = Thread(target=peresdacha).start()
