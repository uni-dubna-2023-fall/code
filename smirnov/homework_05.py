from uuid import uuid4
import threading
from queue import Queue, Empty
import random


class Worker:
    def __init__(self, task_list, result_list):
        self.result_list = result_list
        self.task_list = task_list
        self.lens = len(self.task_list)
        self.line = []
        self.column = []
        self.i = 0
        self.j = 0
        self.task_id = ''
        self.c = 0
        self.result = []

    def run(self):
        p = random.randint(0, self.lens - 1)
        self.task_queue = self.task_list[p][1]
        task = self.task_queue.get()
        self.line = task[0]
        self.column = task[1]
        self.i = task[2]
        self.j = task[3]
        self.task_id = self.task_list[p][0]
        res = 0
        n = len(self.line)
        for i in range(n):
            res += self.line[i] * self.column[i]
        self.c = res
        self.result = [self.c, self.i, self.j, self.task_id]
        for i in range(len(self.result_list)):
            if self.result_list[i][0] == self.task_id:
                self.result_list[i][1].put(self.result)


class Manager:
    def __init__(self):
        self.task_list = []
        self.threading_list = []
        self.result_list = []
        self.result_queue = Queue()
        self.cpu_count = 8

    def run(self):
        for i in range(self.cpu_count):
            w = Worker(self.task_list, self.result_list)
            t = threading.Thread(target=w.run)
            self.threading_list.append(t)
            t.start()

    def stop(self):
        for i in range(len(self.threading_list)):
            self.threading_list[i].join()

    def add_task(self, matrix_a, matrix_b):
        self.task_queue = Queue()
        task_id = str(uuid4())
        lens = len(matrix_a)
        for i in range(lens):
            for j in range(lens):
                new_task = [matrix_a[i], matrix_b[j], i, j]
                self.task_queue.put(new_task)
        a = [task_id, self.task_queue, lens]
        b = [task_id, self.result_queue, lens]
        self.task_list.append(a)
        self.result_list.append(b)
        return task_id

    def status_task(self, task_id):
        for i in range(len(self.task_list)):
            if self.task_list[i][0] == task_id:
                if self.task_list[i][1] is Empty:
                    return 'running'
        for i in range(len(self.task_list)):
            if self.task_list[i][0] == task_id:
                if len(self.task_list[i][1]) == len(self.task_list[i][2]):
                    return 'finishing'

    def get_result(self, task_id):
        number = 0
        lens = 0
        result = []
        for i in range(len(self.task_list)):
            if self.task_list[i][0] == task_id:
                lens = self.task_list[i][2]
                i = number
        for i in range(lens):
            row = []
            for j in range(lens):
                a = self.task_list[j][1].get()
                row.append(a)
            result.append(row)
        return result

    def remove_task(self, task_id):
        for i in range(len(self.task_list)):
            if self.task_list[i][0] == task_id:
                self.task_list.pop(i)
        return task_id

    def list_tasks(self):
        return self.task_list
