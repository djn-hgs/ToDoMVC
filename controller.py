import model, view

class ToDoController:
    def __init__(self, base_model: model.TaskList, base_view: view.ToDoView):
        self.model = base_model
        self.view = base_view

    def mainloop(self):
        while True:
            self.view.list_tasks(self.model)

            action = self.view.get_action()

            if action == 'A':
                title, due_date = self.view.input_task()

                self.model.add(
                    model.Task(
                        title=title,
                        due_date=due_date
                    )
                )

            elif action == 'D':
                task_index = self.view.choose_task(self.model)

                self.model.remove_task(task_index)

            elif action == 'M':
                task_index = self.view.choose_task(self.model)

                self.model.mark_done(task_index)


if __name__ == '__main__':
    model = model.TaskList()
    view = view.ToDoView()
    controller = ToDoController(model, view)
    controller.mainloop()
