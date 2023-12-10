from multiprocessing import Process, Manager
from flask import Flask, request, jsonify

app = Flask(__name__)


class MultiplyMatrix:
    def __init__(self):
        self.manager = Manager()
        self.tasks = self.manager.dict()

    def create_task(self, matrix_a, matrix_b):
        task_id = str(len(self.tasks) + 1)
        self.tasks[task_id] = {
            'status': 'running',
            'result': None
        }
        process = Process(target=self.multiply,
                          args=(task_id, matrix_a, matrix_b))
        process.start()
        return task_id

    def multiply(self, task_id, matrix_a, matrix_b):
        result = [[0] * len(matrix_b[0]) for _ in range(len(matrix_a))]
        for i in range(len(matrix_a)):
            for j in range(len(matrix_b[0])):
                for k in range(len(matrix_b)):
                    result[i][j] += matrix_a[i][k] * matrix_b[k][j]

        self.tasks[task_id]['status'] = 'finished'
        self.tasks[task_id]['result'] = result

    def get_result(self, task_id):
        if self.tasks[task_id]['status'] == 'finished':
            return self.tasks[task_id]['result']
        else:
            return None

    def get_status(self, task_id):
        return self.tasks[task_id]['status']

    def remove_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]


multiply_matrix = MultiplyMatrix()


@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    matrix_a = data['matrix_a']
    matrix_b = data['matrix_b']
    task_id = multiply_matrix.create_task(matrix_a, matrix_b)
    return jsonify({'task_id': task_id, 'status': 'running'})


@app.route('/status/<task_id>', methods=['GET'])
def status_task(task_id):
    status = multiply_matrix.get_status(task_id)
    return jsonify({'task_id': task_id, 'status': status})


@app.route('/tasks', methods=['GET'])
def list_task():
    tasks = list(multiply_matrix.tasks.keys())
    return jsonify(tasks)


@app.route('/result/<task_id>', methods=['GET'])
def get_result(task_id):
    result = multiply_matrix.get_result(task_id)
    if result is None:
        return jsonify({'task_id': task_id, 'result': None})
    else:
        return jsonify({'task_id': task_id, 'result': result})


@app.route('/remove/<task_id>', methods=['DELETE'])
def remove_task(task_id):
    multiply_matrix.remove_task(task_id)
    return jsonify({'task_id': task_id, 'status': 'ok'})


if __name__ == '__main__':
    app.run()
