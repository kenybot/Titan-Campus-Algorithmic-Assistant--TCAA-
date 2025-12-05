import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk
from tkinter import messagebox
from backend.study_planner.greedy_scheduler import greedy_scheduler

# input to add all the tasks that we want
# for it we want, name time ,value


#Bottom output will

task_entries = []


def add_task_row(input_frame,middle_font):

    row = len(task_entries) + 1

    name = tk.Entry(input_frame, width= 15,font=middle_font)
    time = tk.Entry(input_frame, width= 15,font=middle_font)
    value = tk.Entry(input_frame, width= 15,font=middle_font)

    
    name.grid(row=row, column=0,padx=5,pady=2)
    time.grid(row=row ,column=1,padx=5,pady=2)
    value.grid(row=row ,column=2,padx=5,pady=2)
    
    task_entries.append((name,time,value))

def clear_tasks(input_frame,middle_font):
    for entry_set in task_entries:
        for e in entry_set:
            e.destroy()
    task_entries.clear()

    for _ in range(3):
        add_task_row(input_frame,middle_font)

def show_tasks(output_text):
    output_text.delete("1.0",tk.END)

    for i, (name,time,value) in enumerate(task_entries, start=1):
        task_name = name.get()
        task_time = time.get()
        task_value = value.get()
        output_text.insert(tk.END, f"Task {i}: {task_name}, Time: {task_time}, Value: {task_value}\n")


def create_nodes_ui_planner(parent_frame):
    
    FRAME_COLOR = "#0B1D3A"
    TEXT_COLOR = "white"
    FADE_COLOR = '#182F53'

    smallmid_font = tkFont.Font(family="Museo Sans 900", size=12, weight="bold")
    middle_font = tkFont.Font(family="Museo Sans 700", size=18, weight="bold")
    small_font = tkFont.Font(family="Museo Sans 100", size=10)

    # Use a Frame instead of Canvas for inputs
    input_frame = tk.Frame(parent_frame, bg=FADE_COLOR,height=400,width=300)
    input_frame.grid(row=0, column=0, padx=20, pady=(20, 5), sticky="n")

    output_frame = tk.Frame(parent_frame,bg=FADE_COLOR,height=400,width=300)
    output_frame.grid(row=0,column=1,padx=20, pady=(20, 5), sticky="n")
    output_frame.grid_propagate(False)

    #text

    output_text = tk.Text(output_frame, height=20, width=40, bg=FADE_COLOR,fg="white", font=small_font)
    output_text.grid(row=1,column=0,padx=10,pady=10,sticky="nsew")

    # scrollbar = tk.Scrollbar(output_frame, command=output_text.yview)
    # scrollbar.pack(side="right",fill="y")
    # output_text.config(yscrollcommand=scrollbar.set)

    semi_output_frame = tk.Frame(output_frame,bg="white",width=300,height=20)
    semi_output_frame.grid(row=0,column=0, sticky="n")
    tk.Button(output_frame,text="Show Tasks", command=lambda:show_tasks(output_text),bg="green",fg="white").grid(row=2,column=0,pady=5)

    tk.Label(semi_output_frame,text="Optimal Schedule", fg=TEXT_COLOR,bg=FRAME_COLOR,font=middle_font).grid(row=0,column=0)

    tk.Label(input_frame, text="Task", fg=TEXT_COLOR, bg=FADE_COLOR).grid(row=0, column=0)
    tk.Label(input_frame, text="Time", fg=TEXT_COLOR, bg=FADE_COLOR).grid(row=0, column=1)
    tk.Label(input_frame, text="Value", fg=TEXT_COLOR, bg=FADE_COLOR).grid(row=0, column=2)

    #button to add new task row
    tk.Button(input_frame, text="+ Add Task", command=lambda: add_task_row(input_frame,middle_font),bg=FRAME_COLOR,fg="white").grid(row=999, column=0, columnspan=3, pady=10)
    tk.Button(input_frame, text=" Clear Tasks", command=lambda:clear_tasks(input_frame,middle_font),bg=FRAME_COLOR,fg="white").grid(row=1000, column=0, columnspan=3, pady=10)

    add_task_row(input_frame,middle_font)
    add_task_row(input_frame,middle_font)
    add_task_row(input_frame,middle_font)
    
