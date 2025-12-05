

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




def knapsack(tasks, available_time):
    n = len(tasks)
    # DP table: rows = tasks, cols = time capacity
    dp = [[0] * (available_time + 1) for _ in range(n + 1)]

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
    # Build table
    for i in range(1, n + 1):
        task = tasks[i - 1]
        t = task["time"]
        v = task["value"]
        for w in range(available_time + 1):
            if t <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - t] + v)
            else:
                dp[i][w] = dp[i - 1][w]

    # Backtrack to find chosen tasks
    chosen = []
    w = available_time
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            task = tasks[i - 1]
            chosen.append(task)
            w -= task["time"]

    total_value = dp[n][available_time]
    total_time = sum(t["time"] for t in chosen)

    return chosen[::-1], total_time, total_value



if __name__ == "__main__":

    result,time,value = knapsack(tasks=tasks,available_time=150)
    for task in result:
        print(f"- {task['name']} (time {task['time']}, value {task['value']})")

    print(f"Total value: {value}, Total time: {time}")