import json
import multiprocessing
from flask import Flask, request

app = Flask(__name__)


class Manager:
    def __init__(self):
        self.tasks = {}
        self.results = {}

    def start_task(self, matrix_a, matrix_b):
        task_id = str(len(self.tasks) + 1)
        self.tasks[task_id] = (matrix_a, matrix_b)
        return task_id

    def get_task_status(self, task_id):
        if task_id in self.results:
            return 'finished'
        elif task_id in self.tasks:
            return 'running'

    def get_task_result(self, task_id):
        if task_id in self.results:
            return self.results[task_id]

    def remove_task(self, task_id):
        if task_id in self.results:
            del self.results[task_id]

    def get_all_tasks(self):
        return list(self.tasks.keys())

    def run_tasks(self):
        with multiprocessing.Pool() as pool:
            results = pool.map(self._multiply_matrices, self.tasks.values())

        for i, task_id in enumerate(self.tasks):
            self.results[task_id] = results[i]

    def _multiply_matrices(self, matrices):
        matrix_a, matrix_b = matrices
        result = []
        element_result = 0
        for row_a in matrix_a:
            row_result = []
            for col_b in zip(*matrix_b):
                for x, y in zip(row_a, col_b):
                    element_result += x * y
                row_result.append(element_result)
            result.append(row_result)
        return result


matrix_multiplier = Manager()


@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    matrix_a = data['matrix_a']
    matrix_b = data['matrix_b']
    task_id = matrix_multiplier.start_task(matrix_a, matrix_b)
    response = {'task_id': task_id, 'status': 'running'}
    return json.dumps(response)


@app.route('/status/<task_id>', methods=['GET'])
def status_task(task_id):
    status = matrix_multiplier.get_task_status(task_id)
    if status is not None:
        response = {'task_id': task_id, 'status': status}
    else:
        response = {'error': 'The task was not found'}
    return json.dumps(response)


@app.route('/tasks', methods=['GET'])
def list_tasks():
    tasks = matrix_multiplier.get_all_tasks()
    return json.dumps(tasks)


@app.route('/result/<task_id>', methods=['GET'])
def get_result(task_id):
    result = matrix_multiplier.get_task_result(task_id)
    if result is not None:
        response = {'task_id': task_id, 'result': result}
    else:
        response = {'error': 'The task was not found'}
    return json.dumps(response)


@app.route('/remove/<task_id>', methods=['DELETE'])
def remove_task(task_id):
    matrix_multiplier.remove_task(task_id)
    response = {'task_id': task_id, 'status': 'ok'}
    return json.dumps(response)


if __name__ == '__main__':
    app.run()
