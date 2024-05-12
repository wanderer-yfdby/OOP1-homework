# Создай класс `Task`, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.
class Task():
    def __init__(self):
        self.tasks = []
    def add_task(self, deadline, description):
        self.tasks.append({'deadline': deadline, 'description': description,
                           "status": "не выполнено"})
    def complete_tasks(self, description):
        for task in self.tasks:
            if task['description'] == description:
                task['status'] = "Выполнено"
                print(f"\nЗадача {description} выполнена")
            else:
                print(f"Смотри список задач выше")
    def show_tasks(self):
        print("Текущие задачи:")
        for task in self.tasks:
            if task['status'] == "не выполнено":
                print(f"{task['description']} - {task['deadline']}")

task1 = Task()
task1.add_task("09.05.24", "Поздравить с Днем Победы")
task1.add_task("10.05.24", "Сходить в магазин")
task1.add_task("12.05.24" , "Сделать домашнее задание")

task1.show_tasks()

task1.complete_tasks("Поздравить с Днем Победы")
