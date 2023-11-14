import datetime
from dataclasses import dataclass, field


@dataclass
class Task:
    title: str
    done: bool = False
    due_date: datetime.date = datetime.date.today()

    def mark_done(self):
        self.done = True

    def mark_not_done(self):
        self.done = False

    def get_status(self):
        return self.done

    def set_due_date(self, date: datetime.date=datetime.date.today()):
        self.due_date = date

    def get_due_date(self):
        return self.due_date

    def __repr__(self):
        if self.done:
            status = 'X'
        else:
            status = ' '

        return f'{self.due_date}: [{status}] {self.title}'


@dataclass
class TaskList:
    task_list: [Task] = field(default_factory=list)

    def add(self, task: Task):
        self.task_list.append(task)

    def get(self, index: int):
        return self.task_list[index]

    def length(self):
        return len(self.task_list)

    def mark_done(self, index: int):
        self.task_list[index].mark_done()

    def mark_not_done(self, index: int):
        self.task_list[index].mark_not_done()

    def get_status(self, index: int):
        return self.task_list[index].get_status()

    def set_due_date(self, index: int, date: datetime.date = datetime.date.today()):
        self.task_list[index].set_due_date(date)

    def get_due_date(self, index: int):
        return self.task_list[index].due_date

    def is_empty(self):
        return not bool(self.task_list)

    def remove_task(self, index):
        self.task_list.pop(index)

    def __iter__(self):
        return self.task_list.__iter__()