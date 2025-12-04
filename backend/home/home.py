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


def create_home_ui(parent_frame, fade_color, small_font):


    canvas = tk.Canvas(parent_frame, width=200,height=300, bg=fade_color)
    canvas.grid(row=0,column=0,padx=20,pady=(20,5))

    current_time = get_time()
    time_label = tk.Label(canvas,text=current_time,font=small_font,fg="white",justify="center",bg=fade_color)
    canvas.create_window(100, 10, window=time_label, anchor="n")

    
    update_time(time_label,parent_frame)