status = {1: True, 2: False}
tasks = {
    "001": "Start planning my application",
    "002": "Write some code",
}


def cross_out_task(taskId):
    done = input("Done? Y or N: ").lower()
    if done == "y":
        status[taskId] = True
        print(f"Task {taskId} marked as completed.")
    else:
        print(f"Task {taskId} not marked as completed.")


taskID = input("Which task you want to cross")
cross_out_task(taskID)
