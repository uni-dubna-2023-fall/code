import multiprocessing
from flask import Flask, request, jsonify


class MatrixMultiplier:
    def __init__(self):
        self.tasks = {}
        self.task_id = 0

    def multiply_matrices(self, a, b):
        result = []
        for row_a in a:
            row = [sum(x * y for x, y in zip(row_a, col_b))
                   for col_b in zip(*b)]
            result.append(row)
            return result

    def add_task(self, a, b):
        task_id = str(self.task_id)
        self.task_id += 1
        process = multiprocessing.Process(target=self.process_task,
                                          args=(task_id, a, b))
        process.start()
        self.tasks[task_id] = {'process': process,
                               'status': 'running',
                               'result': None}
        return task_id

    def process_task(self, task_id, a, b):
        result = self.multiply_matrices(a, b)
        task = self.tasks[task_id]
        task['result'], task['status'] = result, 'finished'

    def get_status(self, task_id):
        return self.tasks.get(task_id, {}).get('status')

    def get_result(self, task_id):
        task = self.tasks.get(task_id, {})
        return task['result'] if task.get('status') == 'finished' else None

    def remove_task(self, task_id):
        return self.tasks.pop(task_id, None)

    def list_tasks(self):
        return list(self.tasks.keys())


app = Flask(__name__)
mm = MatrixMultiplier()


@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    a, b = data.get('matrix_a'), data.get('matrix_b')
    if a is None or b is None:
        return jsonify({'error': 'Invalid input'}), 400

    task_id = mm.add_task(a, b)
    return jsonify({'task_id': task_id, 'status': 'running'})


@app.route('/status/<task_id>', methods=['GET'])
def status_task(task_id):
    status = mm.get_status(task_id)
    return jsonify({'task_id': task_id, 'status': status}) \
        if status else jsonify({'error': 'Task not found'}), 404


@app.route('/tasks', methods=['GET'])
def list_task():
    return jsonify(mm.list_tasks())


@app.route('/result/<task_id>', methods=['GET'])
def get_result(task_id):
    result = mm.get_result(task_id)
    return jsonify({'task_id': task_id, 'result': result}) \
        if result else jsonify({'error': 'Result not available yet'}), 404


@app.route('/remove/<task_id>', methods=['DELETE'])
def remove_task(task_id):
    removed_task_id = mm.remove_task(task_id)
    response = jsonify({'task_id': removed_task_id, 'status': 'ok'})
    error_response = jsonify({'error': 'Task not found'})
    return response if removed_task_id else error_response, 404


if __name__ == '__main__':
    app.run()
    
