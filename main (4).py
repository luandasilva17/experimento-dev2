class Task:
    def __init__(self, id, description, completed=False):
        self.id = id
        self.description = description
        self.completed = completed

class TaskController:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task_id = len(self.tasks) + 1
        task = Task(task_id, description)
        self.tasks.append(task)

    def mark_as_completed(self, task_id):
        task = next((t for t in self.tasks if t.id == task_id), None)
        if task:
            task.completed = True

    def get_tasks(self):
        return self.tasks

class TaskView:
    def show_tasks(self, tasks):
        print("Tarefas:")
        for task in tasks:
            status = "Feito" if task.completed else "Pendente"
            print(f"{task.id}. {task.description} - {status}")

    def show_message(self, message):
        print(message)

    def get_input(self, prompt):
        return input(prompt).strip()



class TaskApp:
    def __init__(self):
        self.controller = TaskController()
        self.view = TaskView()

    def run(self):
        while True:
            self.view.show_tasks(self.controller.get_tasks())
            command = self.view.get_input("Adicionar (A), Concluir (C) ou Sair (S): ").upper()
            if command == 'A':
                description = self.view.get_input("Digite a descrição da tarefa: ")
                self.controller.add_task(description)
            elif command == 'C':
                task_id = int(self.view.get_input("Digite o ID da tarefa concluída: "))
                self.controller.mark_as_completed(task_id)
            elif command == 'S':
                self.view.show_message("Saindo...")
                break
            else:
                self.view.show_message("Comando inválido")

if __name__ == "__main__":
    app = TaskApp()
    app.run()
