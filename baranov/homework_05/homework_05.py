from flask import Flask, request, jsonify
import numpy as np
import uuid


app = Flask(__name__)


class Manager:
    def __init__(self):
        self.tasks = {}

    def generate_task_id(self):
        return str(uuid.uuid4())

    def run(self):
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
        result = np.dot(matrix_a, matrix_b)
        self.tasks[task_id]['result'] = result
        self.tasks[task_id]['status'] = 'finished'
        return task_id

    def status_task(self, task_id):
        task_status = self.tasks.get(task_id, {"status": "not found"})["status"]
        return task_status

    def get_result(self, task_id):
        task_result = self.tasks.get(task_id, {"result": None})["result"]
        return task_result

    def list_tasks(self):
        return list(self.tasks.keys())


manager = Manager()


@app.route('/multiply', methods=['POST'])
def multiply():
    matrix_data = request.get_json()
    matrix_a = np.array(matrix_data["matrix_a"])
    matrix_b = np.array(matrix_data["matrix_b"])

    task_id = manager.add_task(matrix_a, matrix_b)

    return jsonify({"task_id": task_id, "status": "running"})


@app.route('/status/<task_id>', methods=['GET'])
def status_task(task_id):
    task_status = manager.status_task(int(task_id))
    return jsonify({"task_id": task_id, "status": task_status})


@app.route('/result/<task_id>', methods=['GET'])
def get_result(task_id):
    task_result = manager.get_result(int(task_id))
    return jsonify({"task_id": task_id, "result": task_result})


if __name__ == '__main__':
    manager.run()
