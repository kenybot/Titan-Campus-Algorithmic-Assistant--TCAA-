import time
import tkinter as tk
from datetime import datetime

def get_time():

    return datetime.now().strftime("%H:%M:%S")

def update_time(time_label,parent_frame):
    current_time = datetime.now().strftime("%H:%M:%S")
    if time_label.winfo_exists():
        time_label.config(text=current_time)
        parent_frame.after(1000, update_time, time_label, parent_frame)


def create_home_ui(parent_frame, fade_color, clock_font):


    canvas = tk.Canvas(parent_frame, width=1000, height=100, bg=fade_color)
    canvas.place(relx=0.5, rely=0.5, anchor="center")

    canvas_width = 1000
    canvas_height = 100


    current_time = get_time()
    time_label = tk.Label(canvas,text=current_time,font=clock_font,fg="white",justify="center",bg=fade_color)
    canvas.create_window(canvas_width/2,canvas_height/2, window=time_label, anchor="center")

    
    update_time(time_label,parent_frame)