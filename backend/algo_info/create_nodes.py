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


def create_nodes_ui_algo(parent_frame):
    

    FRAME_COLOR = "#0B1D3A"
    TEXT_COLOR = "white"
    FADE_COLOR = '#182F53'

    bolt_icon = resize_image("gui/build/assets/frame0/bolt.png")

    title_font = tkFont.Font(family="Museo Sans 900", size=18, weight="bold")
    middle_font = tkFont.Font(family="Museo Sans 700", size=16, weight="bold")
    small_font = tkFont.Font(family="Museo Sans 100", size=10)
        
    
    # header = tk.Frame(parent_frame,bg=fade_color,height=50)
    # header.pack(side="top",fill="x")

    # content_title = tk.Label(header, text = " Algorithm Informations ",bg=fade_color,font=small_font,fg='white')
    # content_title.pack(side="top")
    
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
   
    n_np_canvas = tk.Canvas(parent_frame,width=400, height=200, bg=FADE_COLOR)
    n_np_canvas.grid(row=1,column=0,padx=20,pady=(20,5), sticky="nsew")

    complexity_canvas = tk.Canvas(parent_frame, width=200, height=300,bg=FADE_COLOR)
    complexity_canvas.grid(row=0,column=1,padx=20,pady=70,sticky="nsew")

    small_title = tk.Label(complexity_canvas, text="Complexity Classes",
                               font=small_font, bg=FADE_COLOR, fg="white")
    small_title.pack(anchor="nw", padx=5, pady=2)
    
    divider = tk.Frame(complexity_canvas, bg="gray", height=1, width=10)
    divider.pack(anchor="nw", pady=(0, 10))


    parent_frame.grid_columnconfigure(0, weight=1)
    parent_frame.grid_columnconfigure(1, weight=1)
    parent_frame.grid_rowconfigure(0, weight=1)
