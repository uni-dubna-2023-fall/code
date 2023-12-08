import numpy as np
from flask import Flask, jsonify, request
import uuid

app = Flask(__name__)

class Manager:
    def __init__(self):
        self.tasks = {}

    def generate_task_id(self):
        return str(uuid.uuid4())
    
    def run(self):
        while self.is_running:
            app.run()

    def stop(self):
        self.is_running = False

    def add_task(self, matrix_a, matrix_b):
        task_id = self.generate_task_id()
        self.tasks[task_id] = {
            'matrix_a': matrix_a,
            'matrix_b': matrix_b,
            'status': 'running',
            'result': None
        }
        return task_id

    def status_task(self, task_id):
        task = self.tasks.get(task_id)
        if task:
            return task['status']
        else:
            return None

    def get_result(self, task_id):
        task = self.tasks.get(task_id)
        if task and task['status'] == 'finished':
            return task['result']
        else:
            return None

    def remove_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
        return task_id

    def list_tasks(self):
        return list(self.tasks.keys())

    def multiply_matrices(self, task_id):
        task = self.tasks.get(task_id)
        if task and task['status'] == 'running':
            matrix_a = np.array(task['matrix_a'])
            matrix_b = np.array(task['matrix_b'])
            if matrix_a.shape[1] != matrix_b.shape[0]:
                raise ValueError("Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы.")
            task['result'] = np.dot(matrix_a, matrix_b).tolist()
            task['status'] = 'finished'

manager = Manager()

@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    matrix_a = data['matrix_a']
    matrix_b = data['matrix_b']
    task_id = manager.add_task(matrix_a, matrix_b)
    manager.multiply_matrices(task_id)
    return jsonify({'task_id': task_id, 'status': manager.status_task(task_id)})

@app.route('/status/<task_id>', methods=['GET'])
def status_task(task_id):
    return jsonify({'task_id': task_id, 'status': manager.status_task(task_id)})

@app.route('/tasks', methods=['GET'])
def list_task():
    return jsonify(manager.list_tasks())

@app.route('/result/<task_id>', methods=['GET'])
def get_result(task_id):
    result = manager.get_result(task_id)
    if result is not None:
        return jsonify({'task_id': task_id, 'result': result})
    else:
        return jsonify({'task_id': task_id, 'result': 'Вычисление еще не завершено или задача не существует.'})

@app.route('/remove/<task_id>', methods=['DELETE'])
def remove_task(task_id):
    manager.remove_task(task_id)
    return jsonify({'task_id': task_id, 'status': 'ok'})

if __name__ == '__main__':
    app.run()