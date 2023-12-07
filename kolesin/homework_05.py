import json
import multiprocessing
from flask import Flask, request


app = Flask(__name__)


class MatrixMultiplier:

    def __init__(self):
        self.tasks = {}
        self.results = {}
        self.task_queue = multiprocessing.Queue()
        self.result_queue = multiprocessing.Queue()
        self.pool = multiprocessing.Pool()

    def add_task(self, matrix_a, matrix_b):

        task_id = str(len(self.tasks) + 1)
        self.tasks[task_id] = (matrix_a, matrix_b)
        self.task_queue.put((task_id, matrix_a, matrix_b))
        return task_id

    def get_task_status(self, task_id):

        if task_id in self.results:
            return 'finished'
        elif task_id in self.tasks:
            return 'running'

    def get_task_result(self, task_id):

        return self.results.get(task_id)

    def remove_task(self, task_id):

        if task_id in self.results:
            del self.results[task_id]

    def execute_tasks(self):

        while not self.task_queue.empty():
            task_id, matrix_a, matrix_b = self.task_queue.get()
            self.pool.apply_async(self.multiply_matrices,
                                  args=(task_id, matrix_a, matrix_b))
        while not self.result_queue.empty():
            task_id, result = self.result_queue.get()
            self.results[task_id] = result

    def multiply_matrices(self, task_id, matrix_a, matrix_b):

        result = []
        element_result = 0
        for row_a in matrix_a:
            row_result = []
            for col_b in zip(*matrix_b):
                for x, y in zip(row_a, col_b):
                    element_result += x * y
                row_result.append(element_result)
                element_result = 0
            result.append(row_result)
        self.result_queue.put((task_id, result))


matrix_multiplier = MatrixMultiplier()


@app.route('/multiply', methods=['POST'])
def multiply():

    data = request.get_json()
    matrix_a = data['matrix_a']
    matrix_b = data['matrix_b']
    task_id = matrix_multiplier.add_task(matrix_a, matrix_b)
    response = {'task_id': task_id, 'status': 'running'}
    return json.dumps(response)


@app.route('/status/<task_id>', methods=['GET'])
def status_task(task_id):

    status = matrix_multiplier.get_task_status(task_id)
    if status is not None:
        response = {'task_id': task_id, 'status': status}
    else:
        response = {'error': 'Task not found'}
    return json.dumps(response)


@app.route('/tasks', methods=['GET'])
def list_tasks():

    tasks = matrix_multiplier.tasks.keys()
    return json.dumps(list(tasks))


@app.route('/result/<task_id>', methods=['GET'])
def get_result(task_id):

    result = matrix_multiplier.get_task_result(task_id)
    if result is not None:
        response = {'task_id': task_id, 'result': result}
    else:
        response = {'error': 'Task not found'}
    return json.dumps(response)


@app.route('/remove/<task_id>', methods=['DELETE'])
def remove_task(task_id):

    matrix_multiplier.remove_task(task_id)
    response = {'task_id': task_id, 'status': 'ok'}
    return json.dumps(response)


if __name__ == '__main__':
    app.run()
