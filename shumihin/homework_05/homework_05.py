from flask import Flask, request, jsonify

app = Flask(__name__)

class Manager:
    def __init__(self):
        pass

    def run(self):
        while self.is_running:
            app.run()
        pass

    def stop(self):
        self.is_running = False
        pass

    def add_task(self, matrix_a, matrix_b):
        task_id = generate_task_id()
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


@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    matrix_a = data.get('matrix_a')
    matrix_b = data.get('matrix_b')

    if not matrix_a or not matrix_b:
        return jsonify({'error': 'Invalid input'})

    task_id = manager.add_task(matrix_a, matrix_b)

    return jsonify({'task_id': task_id, 'status': 'running'})
    pass


@app.route('/status/<task_id>', methods=['GET'])
def status_task(task_id):
    if task_id not in manager.tasks:
        return jsonify({'error': 'Task not found'})

    task_info = manager.tasks[task_id]

    return jsonify({'task_id': task_id, 'status': task_info['status']})
    pass


@app.route('/tasks', methods=['GET'])
def list_task():
    tasks = manager.get_all_tasks()

    task_ids = [task['task_id'] for task in tasks]

    return jsonify(task_ids)
    pass


@app.route('/result/<task_id>', methods=['GET'])
def get_result(task_id):
    if task_id not in manager.tasks:
        return jsonify({'error': 'Task not found'})

    task_result = manager.get_task_result(task_id)

    return jsonify({'task_id': task_id, 'result': task_result})
    pass


@app.route('/remove/<task_id>', methods=['DELETE'])
def remove_task(task_id):
    if task_id in tasks:
        del tasks[task_id]
        return jsonify({"task_id": task_id, "status": "ok"})
    else:
        return jsonify({"task_id": task_id, "status": "not_found"}), 404
    pass

if __name__ == '__main__':
    app.run()
