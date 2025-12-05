
tasks = [
    {"name": "Review Lecture Notes", "time": 30, "value": 20},
    {"name": "Solve Practice Problems", "time": 60, "value": 50},
    {"name": "Watch Recorded Lecture", "time": 45, "value": 30},
    {"name": "Write Summary Sheet", "time": 40, "value": 35},
    {"name": "Flashcards (Key Terms)", "time": 20, "value": 15},
    {"name": "Group Study Session", "time": 90, "value": 70},
    {"name": "Quiz Yourself (Mock Test)", "time": 60, "value": 55},
    {"name": "Revise Previous Assignment", "time": 50, "value": 40},
    {"name": "Read Textbook Chapter", "time": 80, "value": 45},
    {"name": "Work on Project Draft", "time": 120, "value": 100}
]


def greedy_scheduler(tasks,available_time):
    chosen =[]
    total_time =0
    total_value = 0

    sorted_tasks = sorted(tasks, key=lambda x: x["value"]/x["time"],reverse=True)

    for task in sorted_tasks:
        if task["time"] <= available_time:
            chosen.append(task)
            available_time -= task["time"]
            total_value += task["value"]
            total_time += task["time"]
    return chosen, total_time, total_value


    


if __name__ == "__main__":
    
    result,time,value = greedy_scheduler(tasks=tasks,available_time=150)
    for task in result:
        print(f"- {task['name']} (time {task['time']}, value {task['value']})")

    print(f"Total value: {value}, Total time: {time}")