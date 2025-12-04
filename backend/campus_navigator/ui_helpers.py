from tkinter import messagebox
import tkinter as tk
import random
from tkinter import *
from campus_navigator.node_manager import NodeManager


campus_buildings = [
    ("AF", "Anderson Field"),
    ("BA", "Becker Amphitheater"),
    ("BGC", "Greenhouse Complex"),
    ("CC", "Children's Center"),
    ("CJ", "Carl's Jr."),
    ("CP", "College Park"),
    ("CPAC", "Clayes Performing Arts Center"),
    ("CY", "Corporation Yard"),
    ("CS", "Computer Science"),
    ("DBH", "Dan Black Hall"),
    ("E", "Engineering"),
    ("EC", "Education-Classroom"),
    ("ECS", "Engineering & Computer Science"),
    ("EPS", "Eastside Parking Structure"),
    ("G", "Golleher Alumni House"),
    ("GF", "Goodwin Field"),
    ("H", "Humanities-Social Sciences"),
    ("KHS", "Kinesiology & Health Science"),
    ("LH", "Langsdorf Hall"),
    ("MH", "McCarthy Hall"),
    ("P", "Parking & Transportation Office"),
    ("RH", "Residence Halls"),
    ("PL", "Pollak Library"),
    ("R", "Receiving"),
    ("RGC", "Ruby Gerontology Center"),
    ("SHCC", "Student Health & Counseling Center"),
    ("SGMH", "Mihaylo Hall"),
    ("SH", "Student Housing"),
    ("SRC", "Student Rec Center"),
    ("TB", "Titan Bookstore"),
    ("TG", "Titan Gymnasium"),
    ("TH", "Titan House"),
    ("TS", "Titan Stadium"),
    ("TSU", "Titan Student Union"),
    ("UH", "University Hall"),
    ("UP", "University Police"),
    ("VA", "Visual Arts"),
    ("NPS", "Nutwood Parking Structure"),
    ("SCPS", "State College Parking Structure"),
    ("I", "Visitor Information Center")
]


campus_buildings_abrv = [
    "AF", "BA", "BGC", "CC", "CJ", "CP", "CPAC", "CY", "CS", "DBH", "E", "EC", "ECS",
    "EPS", "G", "GF", "H", "KHS", "LH", "MH", "P", "RH", "PL", "R", "RGC", "SHCC",
    "SGMH", "SH", "SRC", "TB", "TG", "TH", "TS", "TSU", "UH", "UP", "VA", "NPS",
    "SCPS", "I"
]
tk_colors = [
    "snow", "ghost white", "white smoke", "gainsboro", "floral white", "old lace", "linen", "antique white",
    "papaya whip", "blanched almond", "bisque", "peach puff", "navajo white", "lemon chiffon", "mint cream",
    "azure", "alice blue", "lavender", "lavender blush", "misty rose", "white",  "dark slate gray",
    "dim gray", "slate gray", "light slate gray", "light grey", "midnight blue", "navy", "cornflower blue",
    "dark slate blue", "slate blue", "medium slate blue", "light slate blue", "medium blue", "royal blue", "blue",
    "dodger blue", "deep sky blue", "sky blue", "light sky blue", "steel blue", "light steel blue",
    "powder blue", "pale turquoise", "dark turquoise", "medium turquoise", "turquoise", "cyan", "light cyan",
    "cadet blue", "medium aquamarine", "aquamarine", "dark green", "dark olive green", "dark sea green",
    "sea green", "light sea green",
    "green yellow", "lime green", "yellow green", "forest green", "olive drab", "dark khaki", "khaki", "yellow",
    "gold", "light goldenrod", "goldenrod", "dark goldenrod", "rosy brown", "indian red", "saddle brown", "sienna",
    "peru", "burlywood", "beige", "wheat", "sandy brown", "tan", "chocolate", "firebrick", "brown", "dark salmon",
    "salmon", "light salmon", "orange", "dark orange", "coral", "light coral", "tomato", "orange red", "red",
    "hot pink", "deep pink", "pink", "light pink", "pale violet red", "maroon", "medium violet red", "violet red",
    "medium orchid", "dark orchid", "dark violet", "blue violet", "purple", "medium purple", "thistle"
]

def choose_building():
    if not campus_buildings_abrv: #if the campus buildings are empty
        messagebox.showerror("All Chosen", "No more buildings left")
        return None
    building = random.choice(campus_buildings_abrv)
    campus_buildings_abrv.remove(building)
    return building

def edge_creation(root,manager):
    #create widget
    edge_creation= Toplevel(root)
    edge_creation.title("Edge Creation")
    edge_creation.geometry("200x200")
    edge_creation.columnconfigure(0,weight=1)
    #VARIABLES

    distance_var = tk.IntVar()
    time_var = tk.IntVar()
    accessible_var = tk.BooleanVar()


    distance_label = tk.Label(edge_creation, text="Input distance:",font =("Helvetica", 10, "bold"))
    distance_label.grid(row=2, column=0)

    distance_entry = tk.Entry(edge_creation, textvariable= distance_var)
    distance_entry.grid(row=3, column=0)

    time_label = tk.Label(edge_creation, text="Input time:",font =("Helvetica", 10, "bold"))
    time_label.grid(row=4, column=0)

    time_entry = tk.Entry(edge_creation,textvariable=time_var)
    time_entry.grid(row=5, column= 0)

    accessible_label = tk.Label(edge_creation, text= "Accesible?",font =("Helvetica", 10, "bold"))
    accessible_label.grid(row=6, column=0)

    accessible_chk_button = tk.Checkbutton(edge_creation, variable=accessible_var,font =("Helvetica", 10, "bold"))
    accessible_chk_button.grid(row=6, column=1,stick="w",padx=(0,5))

    def submit_edge():
        try:
            distance = int(distance_var.get())
            time = int(time_var.get())
            accessible = accessible_var.get()
            manager.create_edge(distance, time, accessible)
            edge_creation.destroy()
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numeric values for distance and time.")

    submit_button = tk.Button(edge_creation, text="Add Edge", command=submit_edge)
    submit_button.grid(row=7, column=0, columnspan=2, pady=10)

            
def get_mouse_position(canvas):
    x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    y = canvas.winfo_pointery() - canvas.winfo_rooty()
    return x, y

#open menu using right click
def menu_pop_up(event, menu):
    try:
        menu.tk_popup(event.x_root, event.y_root)
    finally:
        menu.grab_release()


def prompt_edge_creation(root,manager):
    if len(manager.selected_nodes) !=2:
        messagebox.showerror("Edge Creation Error", "Please select exactly 2 nodes to create an edge.")
        return
    edge_creation(root,manager)

def traversal_prompt(root, manager, method):
    top = Toplevel(root)
    top.title(f"{method.upper()} Traversal")

    start_var = tk.StringVar()
    goal_var = tk.StringVar()

    tk.Label(top, text="Start Node:").grid(row=0, column=0)
    tk.Entry(top, textvariable=start_var).grid(row=0, column=1)

    tk.Label(top, text="Goal Node:").grid(row=1, column=0)
    tk.Entry(top, textvariable=goal_var).grid(row=1, column=1)

    def run():
        if method == "bfs":
            manager.bfs(start_var.get(), goal_var.get())
        else:
            manager.dfs(start_var.get(), goal_var.get())
        top.destroy()

    tk.Button(top, text="Run", command=run).grid(row=2, column=0, columnspan=2)

def create_nodes_on_canvas():

    # BACKBONE
    root = tk.Tk()
    root.title("Interactive Campus Navigation System")
    root.configure(bg="#D3DAD9")

    #create a main frame

    main_frame = tk.Frame(root)
    main_frame.grid(row=0,column=0,sticky="nw",padx=10,pady=10)
   

    canvas = tk.Canvas(main_frame, width=800, height=600, bg="#44444E")
    canvas.grid(row = 0, column = 0, sticky="nw")

    guide = tk.Label(canvas,text ="Right click to start",fg="white",font =("Helvetica", 10, "bold"),bg="#44444E")

    canvas.create_window(400,50,window=guide)
    
    
    #Buildings list 
    buildings_list_box = Listbox(height=40,width =50,bg="white",font=("Helvetica", 10, "bold"))
    for buildings in campus_buildings:
        buildings_list_box.insert("end", buildings )
    buildings_list_box.grid(row=0, column=1,padx=30, pady=30,sticky="n")

    output_canvas = tk.Canvas(main_frame,width =800, height = 100, bg="#44444E")
    output_canvas.grid(row = 1, column=0, sticky="nw",columnspan=2, pady=(0,10))
    #Class declarations

    manager = NodeManager(canvas)

    accessible_chk = tk.Checkbutton(
    root,
    text="Accessible Only",
    variable=manager.accessible_only_mode,
    font=("Helvetica", 10, "bold"),
    bg="#D3DAD9"
)
    accessible_chk.grid(row=2, column=0, sticky="w", padx=10, pady=5)
    
    """RIGHT CLICK MENU TO ALLOW FOR NODE CREATION/EDGE CREATION , etc"""
    
    open_menu = Menu(root, tearoff = 0)
    open_menu.add_command(label = "Create a node",command=lambda: manager.create_node(*get_mouse_position(canvas),choose_building()))

    open_menu.add_command(label= "Add edges", command = lambda: prompt_edge_creation(root,manager))

    open_menu.add_command(label="Randomize weights", command = manager.randomize_weights)
    open_menu.add_separator()
    open_menu.add_command(label="Start BFS", command=lambda: traversal_prompt(root,manager,"bfs"))
    open_menu.add_command(label="Start DFS", command=lambda: traversal_prompt(root,manager,"dfs"))
    open_menu.add_command(label="Restart canvas", command = manager.restart)

    #OPENS THE MENU USING RIGHT CLICK
    canvas.bind('<Button-3>', lambda event: menu_pop_up(event, open_menu))

    #mainloop, necessary to run the program.
    root.mainloop()