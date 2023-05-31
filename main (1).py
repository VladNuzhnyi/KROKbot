import json
from random import choice


class Task:
    def __init__(self, task, options, right_option):
        self.task = task
        self.options = options
        self.right_option = right_option


class TaskMaker:
    def get_task(self):
        with open('tasks.json', encoding='UTF-8') as file:
            tasks_data = json.load(file)
            task_data = choice(tasks_data)
            return Task(**task_data)