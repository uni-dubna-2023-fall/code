from flask import Flask, url_for, request, jsonify

from multiprocessing import Process, Manager as Mng

# from requests import request

app = Flask(__name__)


def multiply(a, b):
    length = len(a)
    result_matrix = [[0 for i in range(length)] for i in range(length)]
    for i in range(length):
        for j in range(length):
            for k in range(length):
                result_matrix[i][j] += a[i][k] * b[k][j]
    return result_matrix


class Manager:
    def __init__(self):
        self.list_of_task_ids = []
        manager = Mng()
        self.result_list = manager.list()

    def run(self, task_id):
        """Запустить работу вычислительной модели
        """
        print(task_id)
        task_id.start()
        # task_id.join()

    def stop(self, task_id):
        """Остановить работу вычислительной модели
        """
        task_id.terminate()

    def add_task(self, matrix_a, matrix_b):
        print('Ok')
        # task_id = Process(target=lambda: self.result_list.append(multiply(matrix_a, matrix_b, )))
        task_id = Process(target=multiply, args=(matrix_a, matrix_b, ))
        """Передать две матрицы для перемножения и создать новую задачу
        """

        self.run(task_id)
        self.list_of_task_ids.append(task_id)
        return {'task_id': task_id}

    def status_task(self, task_id):
        """Возвращает статус вычислительной задачи 'running' или 'finished'
        """
        if task_id.is_alive():
            return 'running'
        return 'finished'

    def get_result(self, task_id):
        index = self.list_of_task_ids.index(task_id)
        return self.result_list[index]

    def remove_task(self, task_id):
        """Удалить задачу после окончания вычислений
        """
        index = self.list_of_task_ids.index(task_id)
        self.list_of_task_ids.pop(index)
        self.result_list.pop(index)
        return task_id

    def list_tasks(self):
        """Вернуть список всех задач
        """
        return self.list_of_task_ids


@app.route('/')
def index():
    return "Перемножение матриц"


@app.route('/multiply', methods=['POST'])
def multiply():
    """Этот HTTP обработчик должен принимать json строку вида

    {"matrix_a": [[1, 2], [3, 4]], "matrix_b": [[5, 6], [7, 8]]}
    и возвращать json строку вида
    {"task_id": "task_id", "status": "status"}
    """
    data = request.get_json()
    # return data
    id = mng.add_task(data["matrix_a"], data["matrix_b"])
    print(id)
    return data



@app.route('/status/<task_id>', methods=['GET'])
def status_task(task_id):
    """Этот HTTP обработчик должен возвращать json строку вида
    {"task_id": "task_id", "status": "status"}
    """
    return mng.status_task(task_id)


@app.route('/tasks', methods=['GET'])
def list_task():
    """Этот HTTP обработчик должен возвращать json строку вида
    ["task_id_1", "task_id_2"]
    """
    return str(mng.list_tasks())


@app.route('/result/<task_id>', methods=['GET'])
def get_result(task_id):
    """Этот HTTP обработчик должен возвращать json строку вида
    {"task_id": "task_id", "result": [[1, 2], [3, 4]]}
    """
    return mng.get_result(task_id)


@app.route('/remove/<task_id>', methods=['DELETE'])
def remove_task(task_id):
    """Этот HTTP обработчик должен возвращать json строку вида
    {"task_id": "task_id", "status": "ok"}
    """
    mng.remove_task(task_id)
    return {"task_id": task_id, "status": "ok"}


if __name__ == '__main__':
    mng = Manager()
    rs = mng.add_task([[1, 2], [3, 4]], [[5, 6], [7, 8]])
    print(rs)

    app.run(port=8080, host='127.0.0.1')
