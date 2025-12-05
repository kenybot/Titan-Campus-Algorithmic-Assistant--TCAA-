

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

def knapsack(list,available_time):
    n = len(list)

    dp = [[0] * (available_time + 1) for _ in range(n+1)]

    """ VIsualization for this for me
    EXAMPLE
    dp = [[0] * 6 for _ in range(4)]
    [
    [0, 0, 0, 0, 0, 0],  # row 0 (no tasks)
    [0, 0, 0, 0, 0, 0],  # row 1 (task 1 considered)
    [0, 0, 0, 0, 0, 0],  # row 2 (task 2 considered)
    [0, 0, 0, 0, 0, 0]   # row 3 (task 3 considered)
    ]
    
    """








if __name__ == "__main__":

    result,time,value = knapsack(tasks=tasks,available_time=150)
    for task in result:
        print(f"- {task['name']} (time {task['time']}, value {task['value']})")

    print(f"Total value: {value}, Total time: {time}")