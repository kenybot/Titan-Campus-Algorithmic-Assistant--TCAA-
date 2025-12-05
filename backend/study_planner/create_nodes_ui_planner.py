import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk



# input to add all the tasks that we want
# for it we want, name time ,value


#Bottom output will 


def create_nodes_ui_planner(parent_frame):

    #create 3 frames

    task_frame = tk.Frame(parent_frame)
    task_frame.pack(side="left",padx=10,pady=10)

    output_frame = tk.Frame(parent_frame)
    output_frame.pack(side="right", padx=10, pady=10)
