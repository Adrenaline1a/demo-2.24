import random
from threading import Lock, Thread
from queue import Queue


"""
Сдача сесии:
В лице производителя - список преподавателей, дающие задания студенту;
В лице потребителя - студент, сдающий соответсвующие работы преподавателям.
"""


def zachet():
    l = []
    print("\t\tЗачётная книжка")
    while not q2.empty():
        s = q2.get()
        print(f"Преподаватель: {s[0]} id дисциплины: {s[1]} оценка: {s[2]}")
        l.append(s[2])
        if q2.empty():
            break
    if 2 in l:
        print('Студент будет отчислен')
    elif 3 in l:
        print('Студент не будет получать стипендию')
    elif 4 in l:
        print('Студент будет получать обучную стипендию')
    else:
        print('Студент будет получать повышенную стипендию')


def peresdacha():
    lock.acquire()
    ls = []
    while not qe.empty():
        s = qe.get()
        r = random.randint(2,5)
        print(f"Студент пересдал дисциплину с id: {s[1]} преподавателю {s[0]} с оценкой {r}")
        ls.append(
            {
                "id": s[1],
                "Преподаватель": s[0],
                "Оценка": r
            }
        )
    for i in ls:
        q2.put([i["Преподаватель"], i["id"], i["Оценка"]])
    lock.release()
    zachet()


def consumer():
    lock.acquire()
    lst = []
    while not q.empty():
        s = q.get()
        r = random.randint(2,5)
        print(f"Студент сдал дисциплину с id: {s[1]} преподавателю {s[0]} с оценкой {r}")
        lst.append(
            {
                "id": s[1],
                "Преподаватель": s[0],
                "Оценка": r
            }
        )
    for i in lst:
        if i["Оценка"] == 2:
            print(f"Студент не сдал дисциплину с id: {i['id']} и отправляется на пересдачу")
            qe.put([i["Преподаватель"], i["id"]])
        else:
            q2.put([i["Преподаватель"], i["id"], i["Оценка"]])
    lock.release()


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
    q2 = Queue()
    th1 = Thread(target=producer(lst)).start()
    th2 = Thread(target=consumer).start()
    th3 = Thread(target=peresdacha).start()
