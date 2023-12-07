from flask import Flask, request, jsonify
from multiprocessing import Process, Queue

app = Flask(__name__)


class MatrixMultiplier:
    def __init__(self):
        self.tasks = {}
        self.task_counter = 0
        self.queue = Queue()

    def process_task(self, task_id, matrix_a, matrix_b):
        result = self.multiply_matrices(matrix_a, matrix_b)
        self.queue.put((task_id, result))

    def multiply_matrices(self, matrix_a, matrix_b):
        pass

    def add_task(self, matrix_a, matrix_b):
        task_id = str(self.task_counter)
        self.task_counter += 1
        task_process = Process(
            target=self.process_task,
            args=(task_id, matrix_a, matrix_b))
        task_process.start()
        self.tasks[task_id] = task_process
        return task_id

    def status_task(self, task_id):
        if task_id in self.tasks:
            task_process = self.tasks[task_id]
            if task_process.is_alive():
                return 'running'
            else:
                return 'finished'
        else:
            return None

    def get_result(self, task_id):
        if task_id in self.tasks:
            task_process = self.tasks[task_id]
            if not task_process.is_alive():
                task_process.join()
                result = self.queue.get()
                del self.tasks[task_id]
                return result
        return None

    def remove_task(self, task_id):
        if task_id in self.tasks:
            task_process = self.tasks[task_id]
            if not task_process.is_alive():
                task_process.join()
                del self.tasks[task_id]
                return task_id
        return None

    def list_tasks(self):
        return list(self.tasks.keys())


matrix_multiplier = MatrixMultiplier()


@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    matrix_a = data['matrix_a']
    matrix_b = data['matrix_b']
    task_id = matrix_multiplier.add_task(matrix_a, matrix_b)
    return jsonify({'task_id': task_id, 'status': 'running'})


@app.route('/status/<task_id>', methods=['GET'])
def status_task(task_id):
    status = matrix_multiplier.status_task(task_id)
    if status is not None:
        return jsonify({'task_id': task_id, 'status': status})
    else:
        return jsonify({'error': 'Task not found'})


@app.route('/tasks', methods=['GET'])
def list_task():
    tasks = matrix_multiplier.list_tasks()
    return jsonify(tasks)


@app.route('/result/<task_id>', methods=['GET'])
def get_result(task_id):
    result = matrix_multiplier.get_result(task_id)
    if result is not None:
        return jsonify({'task_id': task_id, 'result': result})
    else:
        return jsonify({'error': 'Task not found'})


@app.route('/remove/<task_id>', methods=['DELETE'])
def remove_task(task_id):
    removed_task_id = matrix_multiplier.remove_task(task_id)
    if removed_task_id is not None:
        return jsonify({'task_id': removed_task_id, 'status': 'ok'})
    else:
        return jsonify({'error': 'Task not found'})


if __name__ == '__main__':
    app.run()
