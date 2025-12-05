import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk

def resize_image(png_file, size=(20, 20)):
        try:
            temp = Image.open(png_file)
            temp = temp.resize(size, Image.Resampling.LANCZOS)
            resized_image = ImageTk.PhotoImage(temp)
            return resized_image
        except Exception as e:
            print(f"Image load error: {png_file}, {e}")
            return None
        
def populate_complex_classes(canvas,small_font, title_font):
    x_pad = 10
    y_start =70
    line_height = 25
    FRAME_COLOR = "#0B1D3A"
    def add_header(text, y):
        text_id = canvas.create_text(
            x_pad, y,
            text=text, font=title_font, fill="white", anchor="nw"
        )
        x1, y1, x2, y2 = canvas.bbox(text_id)
        canvas.create_rectangle(x1, y1, x2, y2,outline="")
        canvas.tag_raise(text_id)
        return y + line_height


    def add_entry(text, y):
        entry = text
        canvas.create_text(x_pad + 15, y+2, text=entry, font=small_font, fill="white", anchor="nw")
        return y + line_height
    

    def add_entry(text, y):
        entry = text
        # canvas.create_text(x_pad + 20, y+2, text=entry, font=small_font, fill="white", anchor="nw")
        text_id = canvas.create_text(
            x_pad, y,
            text=entry, font=small_font, fill="white", anchor="nw"
        )
        x1, y1, x2, y2 = canvas.bbox(text_id)
        canvas.create_rectangle(x1, y1, x2, y2, fill=FRAME_COLOR, outline=FRAME_COLOR,width=1)
        canvas.tag_raise(text_id)
        return y + line_height

    

    y = y_start
    #FIRST ONE.
    y = add_header("O(1) - Constant Time", y)
    y = add_entry("Best case performance. Execution time doesn't depend on input size.", y)

    y = add_header("O(log n) - Logarithmic", y)
    y = add_entry("Divides problem in half each iteration. Very efficient for large inputs.", y)

    y = add_header("O(n) - Linear Time", y)
    y = add_entry("Execution time grows linearly with input size. Common in many algorithms.", y)

    y = add_header("O(n log n) - Linearithmic", y)
    y = add_entry("Optimal for comparison-based sorting. Efficient divide-and-conquer.", y)

    y = add_header("O(n²) - Quadratic", y)
    y = add_entry("Nested iterations. Can be slow for large inputs but simple to implement.", y)

    y = add_header("O(2ⁿ) - Exponential", y)
    y = add_entry("Grows extremely fast. Usually requires optimization or approximation.", y)

     

def populate_time_complexities(canvas, small_font, title_font):
    FRAME_COLOR = "#0B1D3A"
    x_pad = 10
    y_start = 70
    line_height = 25

    def add_header(text, y):
        text_id = canvas.create_text(
            x_pad, y,
            text=text, font=title_font, fill="white", anchor="nw"
        )
        x1, y1, x2, y2 = canvas.bbox(text_id)
        canvas.create_rectangle(x1, y1, x2, y2, outline="")
        canvas.tag_raise(text_id)
        return y + line_height


    def add_entry(name, time, space, y):
        entry = f"{name}: Time: {time}, Space: {space}"
        # canvas.create_text(x_pad + 20, y+2, text=entry, font=small_font, fill="white", anchor="nw")
        text_id = canvas.create_text(
            x_pad, y,
            text=entry, font=title_font, fill="white", anchor="nw"
        )
        x1, y1, x2, y2 = canvas.bbox(text_id)
        canvas.create_rectangle(x1, y1, x2, y2, fill=FRAME_COLOR, outline=FRAME_COLOR,width=1)
        canvas.tag_raise(text_id)
        return y + line_height

    y = y_start

    # Graph Traversal
    y = add_header("Graph Traversal", y)
    y = add_entry("BFS", "O(V + E)", "O(V)", y)
    y = add_entry("DFS", "O(V + E)", "O(V)", y)

    # Shortest Path
    y = add_header("Shortest Path", y)
    y = add_entry("Dijkstra", "O((V + E) log V)", "O(V)", y)

    # Minimum Spanning Tree
    y = add_header("Minimum Spanning Tree", y)
    y = add_entry("Prim's MST", "O(E log V)", "O(V)", y)

    # Optimization
    y = add_header("Optimization", y)
    y = add_entry("Greedy Scheduling", "O(n log n)", "O(1)", y)

    # Dynamic Programming
    y = add_header("Dynamic Programming", y)
    y = add_entry("0/1 Knapsack", "O(n × W)", "O(n × W)", y)

    # String Matching
    y = add_header("String Matching", y)
    y = add_entry("Naive Search", "O(n × m)", "O(1)", y)
    y = add_entry("Rabin-Karp", "O(n + m)", "O(1)", y)
    y = add_entry("KMP", "O(n + m)", "O(m)", y)

def create_nodes_ui_algo(parent_frame):
    
    FRAME_COLOR = "#0B1D3A"
    TEXT_COLOR = "white"
    FADE_COLOR = '#182F53'

    bolt_icon = resize_image("gui/build/assets/frame0/bolt.png")
    complex_icon = resize_image("gui/build/assets/frame0/chat-arrow-grow.png")

    smallmid_font = tkFont.Font(family="Museo Sans 900", size=12, weight="bold")
    middle_font = tkFont.Font(family="Museo Sans 700", size=16, weight="bold")
    small_font = tkFont.Font(family="Museo Sans 100", size=10)
    
    # --- Time Complexity Section ---

    time_comp_canvas = tk.Canvas(parent_frame, width=200, height=300, bg=FADE_COLOR)
    time_comp_canvas.grid(row=0,column=0,padx=20,pady=(20,5),sticky="nsew")


    time_comp_label = tk.Label(time_comp_canvas,image=bolt_icon,text="Time Complexities",font=middle_font,bg=FADE_COLOR,fg="white",justify="left",compound="left")
    time_comp_label.pack(anchor="nw",padx=5,pady=2)
    time_comp_label.image = bolt_icon

    small_title = tk.Label(time_comp_canvas, text="Time complexities and complexity classes",
                               font=small_font, bg=FADE_COLOR, fg="white")
    small_title.pack(anchor="nw", padx=5, pady=2)

    divider = tk.Frame(time_comp_canvas, bg="gray", height=1, width=400)
    divider.pack(anchor="nw", pady=(0, 10))

    populate_time_complexities(time_comp_canvas,small_font=smallmid_font,title_font=small_font)

    # --- N VS NP Section ---

    n_np_canvas = tk.Canvas(parent_frame,width=400, height=200, bg=FADE_COLOR)
    n_np_canvas.grid(row=1,column=0,padx=20,pady=(20,5), sticky="nsew")



    

    # --- Complexity Section ---

    complexity_canvas = tk.Canvas(parent_frame, width=200, height=300,bg=FADE_COLOR)
    complexity_canvas.grid(row=0,column=1,padx=20,pady=(20,5),sticky="nsew")

    complex_label = tk.Label(complexity_canvas,image=complex_icon, text="Complexity Classes",
                               font=middle_font, bg=FADE_COLOR, fg="white",compound="left",padx=10)
    complex_label.pack(anchor="nw", padx=5, pady=2)
    complex_label.image = complex_icon

    complex_small_label = tk.Label(complexity_canvas, text="Best to worst case in descending",
                               font=small_font, bg=FADE_COLOR, fg="white")
    complex_small_label.pack(anchor="nw", padx=5, pady=2)


    divider = tk.Frame(complexity_canvas, bg="gray", height=1, width=200)
    divider.pack(anchor="nw", pady=(0, 10))

    populate_complex_classes(complexity_canvas,small_font=small_font,title_font=smallmid_font)
    

    parent_frame.grid_columnconfigure(0, weight=1)
    parent_frame.grid_columnconfigure(1, weight=1)
    parent_frame.grid_rowconfigure(0, weight=1)
