import multiprocessing
import json
from flask import Flask, request
import numpy as np

app = Flask(__name__)


class Manager:

    def __init__(self):
        self.tasks = {}
        self.tasks_counter = 0

    def multiply_matrix(self, matrix_a, matrix_b):
        a = np.array(matrix_a)
        b = np.array(matrix_b)
        result = a.dot(b)
        return result

    def add_task(self, matrix_a, matrix_b):
        task_id = str(self.tasks_counter)
        self.tasks_counter += 1
        self.tasks[task_id] = {
            'status' : 'running',
            'result' : ''
        }

        process = multiprocessing.Process(
            target=self.get_result(),
            args=(task_id, matrix_a, matrix_b)
        )
        process.start()
        return task_id

    def status_task(self, task_id):
        if task_id in self.tasks:
            return self.tasks[task_id]['status']

    def get_result(self, task_id, matrix_a, matrix_b):
        result = self.multiply_matrix(matrix_a, matrix_b)
        self.tasks[task_id]['result'] = result
        self.tasks[task_id]['status'] = 'finished'
        return result

    def remove_task(self, task_id):
        self.tasks.pop(task_id)
        return task_id

    def list_tasks(self):
        list_of_task_ids = self.tasks.keys()
        return list_of_task_ids

manager = Manager()

@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    matrix_a = data['matrix_a']
    matrix_b = data['matrix_b']
    task_id = manager.add_task(matrix_a, matrix_b)
    data_pro = {
        'task_id': task_id,
        'status' : 'running'
    }
    return json.dumps(data_pro)


@app.route('/status/<task_id>', methods=['GET'])
def status_task(task_id):
    data_pro = request.get_json()
    status = manager.status_task(task_id)
    data_pro = {
        'task_id': task_id,
        'status' : status
    }
    return json.dumps(data_pro)


@app.route('/tasks', methods=['GET'])
def list_task():
    tasks = manager.list_tasks()
    return json.dumps(tasks)


@app.route('/result/<task_id>', methods=['GET'])
def get_result(task_id):
    data_pro = request.get_json()
    result = manager.get_result(task_id)
    data_pro = {
        'task_id': task_id,
        'result' : result
    }
    return json.dumps(data_pro)


@app.route('/remove/<task_id>', methods=['DELETE'])
def remove_task(task_id):
    data_pro = request.get_json()
    if task_id in manager.tasks:
        manager.remove_task(task_id)
        data_pro = {
            'task_id': task_id,
            'status' : 'deleted'
        }
    else:
        data_pro = {
            'task_id': 'не найдено'
        }
    return json.dumps(data_pro)
