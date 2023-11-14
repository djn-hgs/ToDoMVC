import datetime

import model


class ToDoView:
    def print_task(self, task: model.Task):
        print(task)

    def list_tasks(self, todo_list: model.TaskList):
        print('Tasks\n')

        for index, task in enumerate(todo_list):
            print(f'{index}:  {task}')

    def choose_task(self, task_list: model.TaskList) -> int:
        print('Tasks:')

        self.list_tasks()

        still_asking = True
        choice = None

        while still_asking:
            chosen_task = input('Choose a task ')

            choice = int(chosen_task)

            if choice in range(task_list.length()):
                still_asking = False

        return choice

    def get_action(self) -> str:
        print(
            '(A)dd task\n'
            '(D)elete task\n'
            '(M)ark done'
            )

        choice = input()

        return choice

    def input_task(self) -> (str, datetime.date):
        title = input('Title: ')
        due_date = input('Date (%d/%m/%y) empty for today: ')

        if due_date == '':
            due_date = datetime.date.today()
        else:
            due_date = datetime.datetime.strptime(due_date, '%d/%m/%y')

        return title, due_date

