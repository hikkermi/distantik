from task_manage.task_manager import TaskManager
from task_manage.database.db import Database

def display_menu():
    print("\n1. Добавить задачу")
    print("2. Показать все задачи")
    print("3. Изменить статус")
    print("4. Удалить задачу")
    print("5. Поиск задач")
    print("6. Выход")

def run_cli():
    task_manager = TaskManager()
    db = Database()

    tasks = db.load_tasks()
    for task in tasks:
        task_manager.tasks[task.id] = task
        task_manager.next_id = max(task_manager.next_id, task.id + 1)

    while True:
        display_menu()
        choice = input("Выберите действие: ")

        if choice == '1':
            title = input("Введите название задачи: ")
            description = input("Введите описание задачи: ")
            task_manager.add_task(title, description)
            db.save_task(task_manager.tasks[task_manager.next_id - 1])
            print("Задача добавлена.")

        elif choice == '2':
            tasks = task_manager.get_all_tasks()
            for task in tasks:
                print(task)

        elif choice == '3':
            task_id = int(input("Введите ID задачи для изменения статуса: "))
            status = input("Введите новый статус (не выполнено, в процессе, выполнено): ")
            task_manager.update_task(task_id, status)
            print("Статус задачи обновлен.")

        elif choice == '4':
            task_id = int(input("Введите ID задачи для удаления: "))
            task_manager.delete_task(task_id)
            print("Задача удалена.")

        elif choice == '5':
            keyword = input("Введите ключевое слово для поиска: ")
            found_tasks = task_manager.search_tasks(keyword)
            for task in found_tasks:
                print(task)

        elif choice == '6':
            db.close()
            break

        else:
            print("Неверный ввод. Пожалуйста, попробуйте снова.")