# Ex7 To do list:
import random

todo_list = []


def get_task():

    task = input("Enter a new task: ")

    return {"task": task, "completed": False}


def display_menu():
    print("\nOptions:")
    print("1. Add Task")
    print("2. Mark Task as Completed")
    print("3. View To-Do List")
    print("4. Punishment Game")
    print("5. Quit")


def display_todo_list():

    print("\nTo-Do List:")

    for index, task in enumerate(todo_list):

        print(
            f"{index + 1}. {task['task']} - {'Completed' if task['completed'] else 'Incomplete'}"
        )


def select_random_exercise():

    exercises = [
        "10 push-ups",
        "20 jumping jacks",
        "15 squats",
        "30-second plank",
        "10 burpees",
        "5-minute brisk walk",
    ]

    return random.choice(exercises)


def punishment_game():

    exercise = select_random_exercise()
    print(f"\nPunishment Game: You must perform the following exercise: {exercise}")
    complete_exercise = input("Did you complete the exercise? (yes/no): ").lower()

    if complete_exercise == "yes":
        print("Exercise completed! Good job!")

    else:
        print("Exercise not completed. Better luck next time!")


def main():
    print("Welcome to the To-Do List Manager!")

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            new_task = get_task()
            todo_list.append(new_task)
            print("Task added successfully!")

        elif choice == "2":
            display_todo_list()
            task_number = int(
                input("Enter the number of the task to mark as completed: ")
            )

            if 1 <= task_number <= len(todo_list):
                todo_list[task_number - 1]["completed"] = True
                print("Task marked as completed!")

            else:
                print("Invalid task number.")

        elif choice == "3":
            display_todo_list()

        elif choice == "4":
            punishment_game()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


main()
