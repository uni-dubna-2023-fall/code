from flask import Flask, request, jsonify
import numpy as np
import multiprocessing
app = Flask(__name__)


class Manager:
    def __init__(self):
        self.tasks = {}
        self.task_counter = 0
        self.pool = multiprocessing.Pool()

    def run(self):
        app.run()

    def stop(self):
        self.pool.close()
        self.pool.join()

    def multiply_matrices(self, matrices):
        matrix_a, matrix_b = matrices
        result = np.dot(matrix_a, matrix_b)
        return result.tolist()

    def add_task(self, matrix_a, matrix_b):
        task_id = str(self.task_counter)
        self.tasks[task_id] = {
            'status': 'running',
            'result': None,
            'task': self.pool.apply_async
            (self.multiply_matrices, args=((matrix_a, matrix_b),))
        }
        self.task_counter += 1
        return task_id

    def status_task(self, task_id):
        task = self.tasks.get(task_id)
        if task:
            if task['task'].ready():
                task['status'] = 'finished'
                task['result'] = task['task'].get()
            return {'task_id': task_id, 'status': task['status']}
        else:
            return {'error': 'Task not found'}

    def get_result(self, task_id):
        task = self.tasks.get(task_id)
        if task and task['status'] == 'finished':
            return {'task_id': task_id, 'result': task['result']}
        else:
            return {'error': 'Task not finished or not found'}

    def remove_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
            return {'task_id': task_id, 'status': 'ok'}
        else:
            return {'error': 'Task not found'}

    def list_tasks(self):
        return list(self.tasks.keys())


manager = Manager()


@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.json
    matrix_a = np.array(data['matrix_a'])
    matrix_b = np.array(data['matrix_b'])
    task_id = manager.add_task(matrix_a, matrix_b)
    return jsonify({'task_id': task_id, 'status': 'running'})


@app.route('/status/<task_id>', methods=['GET'])
def status_task(task_id):
    return jsonify(manager.status_task(task_id))


@app.route('/tasks', methods=['GET'])
def list_task():
    return jsonify(manager.list_tasks())


@app.route('/result/<task_id>', methods=['GET'])
def get_result(task_id):
    return jsonify(manager.get_result(task_id))


@app.route('/remove/<task_id>', methods=['DELETE'])
def remove_task(task_id):
    return jsonify(manager.remove_task(task_id))


if __name__ == '__main__':
    manager.run()
