import tkinter as tk



def create_nodes_ui_algo(parent_frame,fade_color,small_font):
    
    # header = tk.Frame(parent_frame,bg=fade_color,height=50)
    # header.pack(side="top",fill="x")

    # content_title = tk.Label(header, text = " Algorithm Informations ",bg=fade_color,font=small_font,fg='white')
    # content_title.pack(side="top")
    
    time_comp_canvas = tk.Canvas(parent_frame, width=400, height=300, bg=fade_color)
    time_comp_canvas.grid(row=0,column=0,padx=20,pady=(20,5),sticky="nsew")
    x = time_comp_canvas.winfo_width() //2
    y = time_comp_canvas.winfo_height() //2

    time_comp_label = tk.Label(time_comp_canvas, text="Time Complexities",font=small_font,bg=fade_color,fg="white",justify="left")
    time_comp_label.pack(anchor="nw",padx=10,pady=10)
    time_comp_canvas.create_text(250,200,text="Algorithm Insights", font=small_font, fill="white",anchor="w")

    n_np_canvas = tk.Canvas(parent_frame,width=800, height=200, bg=fade_color)
    n_np_canvas.grid(row=1,column=0,padx=20,pady=(20,5), sticky="nsew")
    complexity_canvas = tk.Canvas(parent_frame, width=200, height=300,bg=fade_color)
    complexity_canvas.grid(row=0,column=1,padx=20,pady=(20,5),sticky="nsew")


    parent_frame.grid_columnconfigure(0, weight=1)
    parent_frame.grid_columnconfigure(1, weight=1)
    parent_frame.grid_rowconfigure(0, weight=1)
