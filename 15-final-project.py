# Simple console based To-Do list app
user_choice=-1  # initialised as -1 so it can not be confused with values received from user
initial_flag = 1
tasks = [] # ?is it declaration or definition?  When does the Python allocate the memory


def show_tasks():
    task_index = 0
    for task in tasks:
        print(task +" [" + str(task_index) + "] ") #intiger to string convertion to anable + operator
        task_index +=1

def add_task():
    task = input("Type the task: ")
    tasks.append(task)
    print("Task added!")

def delete_task():
    task_index = int(input('Type the index of task to remove: '))
    if task_index < 0 or task_index > len(tasks) -1:
        print('Wrong index!')
        return # returns nothing, just finishes the function
    tasks.pop(task_index)
    print("Task removed from the list!")

def save_tasks_to_file():
    file = open("tasks.txt" , "w")
    for task in tasks:
        file.write(task + "\n")
    file.close()

def load_tasks_from_file():
    try:
        file = open("tasks.txt")
        for line in file.readlines():
            tasks.append(line.strip()) # .strip method to remove \n that was added to file
        file.close()
    except FileNotFoundError:
        return


load_tasks_from_file()



while user_choice !=5:
    if user_choice == 1:
        initial_flag = 0
        show_tasks()

    if user_choice == 2:
        initial_flag = 0
        add_task()

    if user_choice == 3:
        initial_flag = 0
        delete_task()

    if user_choice == 4:
        initial_flag = 0
        save_tasks_to_file()

    if initial_flag !=1 and user_choice < 1 or user_choice > 5:
        initial_flag = 0
        print("Number out of range")
    

    print()    
    print("1. Show task")
    print("2. Add task")
    print("3. Delete task")
    print("4. Save changes to file")
    print("5. Exit")

    user_choice = int(input("Chose number of option: ")) # int as convertion to integer will be neded
    print()





