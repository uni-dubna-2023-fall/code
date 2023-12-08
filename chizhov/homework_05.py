import multiprocessing
from numpy import matrix
from flask import Flask, request, jsonify


app = Flask(__name__)


class Manager:
    def __init__(self):
        self.tasks = {}
        self.results = {}

    def run(self):
        with multiprocessing.Pool() as pool:
            results = pool.map(self.multiply_matrices, self.tasks.values())

        for index, task_id in enumerate(self.tasks):
            self.results[task_id] = results[index]

    def add_task(self, matrix_a, matrix_b):
        task_id = str(len(self.tasks) + 1)
        self.tasks[task_id] = (matrix_a, matrix_b)
        return task_id

    def status_task(self, task_id):
        if task_id in self.results:
            return 'finished'
        elif task_id in self.tasks:
            return 'running'

    def get_result(self, task_id):
        if task_id in self.results:
            return self.results[task_id]

    def remove_task(self, task_id):
        if task_id in self.results:
            del self.results[task_id]

    def list_tasks(self):
        return list(self.tasks.keys())

    def multiply_matrices(self, matrices):
        matrix_a, matrix_b = matrices
        result = matrix(matrix_a).dot(matrix(matrix_b)).tolist()
        return result


manager = Manager()


@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    matrix_a = data['matrix_a']
    matrix_b = data['matrix_b']
    task_id = manager.add_task(matrix_a, matrix_b)
    response = {'task_id': task_id, 'status': 'running'}
    return jsonify(response)


@app.route('/status/<task_id>', methods=['GET'])
def status_task(task_id):
    status = manager.status_task(task_id)
    if status is not None:
        response = {'task_id': task_id, 'status': status}
    else:
        response = {'error': 'The task was not found'}
    return jsonify(response)


@app.route('/tasks', methods=['GET'])
def list_tasks():
    tasks = manager.list_tasks()
    return jsonify(tasks)


@app.route('/result/<task_id>', methods=['GET'])
def get_result(task_id):
    result = manager.get_result(task_id)
    if result is not None:
        response = {'task_id': task_id, 'result': result}
    else:
        response = {'error': 'The task was not found'}
    return jsonify(response)


@app.route('/remove/<task_id>', methods=['DELETE'])
def remove_task(task_id):
    manager.remove_task(task_id)
    response = {'task_id': task_id, 'status': 'ok'}
    return jsonify(response)


if __name__ == '__main__':
    app.run()
