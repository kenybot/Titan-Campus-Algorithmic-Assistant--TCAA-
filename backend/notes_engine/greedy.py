tasks = [
    ("Math HW", 60, 10),
    ("Read Chapter", 70, 4),
    ("Practice Coding", 140, 5),
]
#"NAME","TIME (1-300 minutes)",VALUE (1-10) importance



def greedy_earliest(tasks, available_time):

    tasks_sorted = sorted(tasks, key=lambda x: x[2]/x[1],reverse=True)
    #basically, for every task in tasks, we are dividing importance with time allocated.
    #We then used the ratio to sort by highest efficiency.

    total_time = 0
    chosen = []

    for task in tasks_sorted:
        if total_time + task[1] <= available_time:
            chosen.append(task)
            total_time += task[1]
    return chosen
            

if __name__ == "__main__":
    tasks = [
    ("Math HW", 60, 10),
    ("Read Chapter", 70, 4),
    ("Practice Coding", 140, 5),
]
    result = greedy_earliest(tasks, 200)
    for tasks in result:
        print(tasks[0] )

    #basically done. just need to add a gui that will add values to a list and we use that list
    # for our algo.