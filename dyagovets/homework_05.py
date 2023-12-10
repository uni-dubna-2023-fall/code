import multiprocessing
import json
from flask import Flask, request

app = Flask(__name__)


class MatrixMultiplier:
    def __init__(self):
        self.tasks = {}
        self.task_id_counter = 0
        self.processes = []

    def multiply_matrices(self, matrix_a, matrix_b):
        result = []
        for i in range(len(matrix_a)):
            row = []
            for j in range(len(matrix_b[0])):
                element = 0
                for k in range(len(matrix_b)):
                    element += matrix_a[i][k] * matrix_b[k][j]
                row.append(element)
            result.append(row)
        return result

    def start_task(self, matrix_a, matrix_b):
        task_id = str(self.task_id_counter)
        self.task_id_counter += 1
        self.tasks[task_id] = {
            'status': 'running',
            'result': None
        }
        process = multiprocessing.Process(
            target=self.run_task,
            args=(task_id, matrix_a, matrix_b)
        )
        self.processes.append(process)
        process.start()
        return task_id

    def run_task(self, task_id, matrix_a, matrix_b):
        result = self.multiply_matrices(matrix_a, matrix_b)
        self.tasks[task_id]['result'] = result
        self.tasks[task_id]['status'] = 'finished'

    def get_task_status(self, task_id):
        if task_id in self.tasks:
            return self.tasks[task_id]['status']
        else:
            return None

    def get_task_result(self, task_id):
        if task_id in self.tasks:
            return self.tasks[task_id]['result']
        else:
            return None

    def remove_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]

    def get_all_tasks(self):
        return list(self.tasks.keys())


matrix_multiplier = MatrixMultiplier()


@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    matrix_a = data['matrix_a']
    matrix_b = data['matrix_b']
    task_id = matrix_multiplier.start_task(matrix_a, matrix_b)
    response_data = {
        'task_id': task_id,
        'status': 'running'
    }
    return json.dumps(response_data)


@app.route('/status/<task_id>', methods=['GET'])
def status_task(task_id):
    status = matrix_multiplier.get_task_status(task_id)
    if status is not None:
        response_data = {
            'task_id': task_id,
            'status': status
        }
    else:
        response_data = {
            'error': 'Task not found'
        }
    return json.dumps(response_data)


@app.route('/tasks', methods=['GET'])
def list_task():
    tasks = matrix_multiplier.get_all_tasks()
    return json.dumps(tasks)


@app.route('/result/<task_id>', methods=['GET'])
def get_result(task_id):
    result = matrix_multiplier.get_task_result(task_id)
    if result is not None:
        response_data = {
            'task_id': task_id,
            'result': result
        }
    else:
        response_data = {
            'error': 'Task not found or not finished'
        }
    return json.dumps(response_data)


@app.route('/remove/<task_id>', methods=['DELETE'])
def remove_task(task_id):
    matrix_multiplier.remove_task(task_id)
    response_data = {
        'task_id': task_id,
        'status': 'ok'
    }
    return json.dumps(response_data)


if __name__ == '__main__':
    app.run()
