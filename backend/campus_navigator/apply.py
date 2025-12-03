#Kendrik Deleoz
#kendrikdeleoz@csu.fullerton.edu
#Project: CPSC 335- Interactive Campus Navigation System.
# 10/22/2025
"""
Create an interactive campus navigation system using BFS and DFS.

1)Graph Creation (campus map)
2) Visualization
3) Dynamic Weights
4) BFS and DFS Implementation
5) Edge Closures
6) Error Handlings.

"""
import tkinter as tk
from tkinter import Tk,Label
from tkinter import *
from tkinter import messagebox
import random

from heapq import heappush, heappop
#global variables
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


class NodeManager:
    def __init__(self,canvas):
        self.canvas = canvas
        self.nodes = []
        self.selected_nodes = []
        self.edges = []
        self.selected_edges = []
        self.bfs_edges = []
        self.dfs_edges = []
        self.closed_edges = []
        self.open_edges = []
        self.non_accesible_edges = []
        self.accessible_only_mode = tk.BooleanVar()

    def create_node(self,x,y,name="Node"):
        node = Node(self.canvas,x,y,name,manager=self)
        print(f"The node {name} has been created at {x},{y}")
        self.nodes.append(node)
        self.canvas.tag_raise("node")
        self.display_output(f"{node.text} has been created at ({x},{y}) with color: {node.original_color}")
    
    def select(self,node):
        if node not in self.selected_nodes:
            self.selected_nodes.append(node)
        self.display_output(f"{node.text} has been selected")

    def deselect(self,node):
        if node in self.selected_nodes:
            self.selected_nodes.remove(node)
            self.canvas.itemconfig(node.rect, fill=node.original_color)
            node.selected = False
        print(node,"has been deselected")
        self.display_output(f"{node.text} has been deselected")

    def create_edge(self, distance, time, accesible=True):
        if len(self.selected_nodes) != 2:
            print("2 nodes need to be selected")
            return
        first_node,second_node = self.selected_nodes
        edge = Edge(self.canvas, first_node, second_node, distance, time, accesible)
        self.edges.append(edge)
        edge.update_state()

        print(f"Edge created between {first_node} and {second_node}")
        self.deselect(first_node)
        self.deselect(second_node)
        self.display_output(f"Edge added: {first_node.text}  ↔ {second_node.text} ({distance}m, {time}min), accesible = {accesible}")
        self.canvas.tag_raise("node")



    def display_output(self,message):
        self.canvas.master.children['!canvas2'].delete("all")
        self.canvas.master.children['!canvas2'].create_text(
            10,10, anchor="nw", text=message,fill="white",font=("Helvectica",10, "bold")
        )

    def randomize_weights(self):
        if not self.edges:
            messagebox.showerror("Empty","No edges available")
        for edge in self.edges:
            edge.distance = random.randint(1,100)
            edge.time = random.randint(1,30)
            self.canvas.itemconfig(edge.label, text=f"{edge.distance}m, {edge.time}min")
        print("Edge weights randomized")
        self.display_output("Edge weights have been randomized")
    
    def restart(self):
        response = messagebox.askquestion("Are you sure?", "Would you like to proceed?")

        if response == "yes":
            for node in self.nodes:
                self.canvas.delete(node.rect)
                self.canvas.delete(node.text_item)
            for edge in self.edges:
                self.canvas.delete(edge.line)
                self.canvas.delete(edge.label)
            
            self.nodes.clear()
            self.selected_nodes.clear()
            self.edges.clear()
            self.selected_edges.clear()

            print("Canvas and graph reset.")
        else:
            return

    def dfs(self, start_name, goal_name):
        for edge in self.edges:
            edge.update_state()
        start = next((n for n in self.nodes if n.text == start_name), None)
        goal = next((n for n in self.nodes if n.text == goal_name), None)

        if not start or not goal:
            messagebox.showerror("Invalid", "Start or goal node not found.")
            return

        # Optional: reset edge colors before traversal
        for edge in self.edges:
            edge.update_state()

        visited = set()
        stack = [(start, [], [start])]  # (current_node, path_edges, path_nodes)

        while stack:
            current, path_edges, path_nodes = stack.pop()
            if current in visited:
                continue
            visited.add(current)

            self.canvas.update()
            self.canvas.after(100)

            if current == goal:
                total_distance = sum(edge.distance for edge in path_edges)
                total_time = sum(edge.time for edge in path_edges)

                for edge in path_edges:
                    self.canvas.itemconfig(edge.line, fill="green")
                self.display_output(
                    f"Path: {' → '.join(n.text for n in path_nodes)}\n"
                    f"Length: {len(path_edges)} edges\n"
                    f"Total Distance: {total_distance}m\n"
                    f"Total Time: {total_time}min")
                return

            for edge in self.get_connected_edges(current):
                neighbor = edge.second_node if edge.first_node == current else edge.first_node
                if neighbor not in visited:
                    stack.append((neighbor, path_edges + [edge], path_nodes + [neighbor]))

        messagebox.showinfo("No Path", "No path found.")

    def dijkstra(self, start_name, goal_name):
        for edge in self.edges:
            edge.update_state()
        
        start = next((n for n in self.nodes if n.text == start_name), None)
        goal = next((n for n in self.nodes if n.text == goal_name), None)

        if not start or not goal:
            messagebox.showerror("Invalid", "Start or goal node not found.")
            return
        pq = [(0,start, [], [start])]
        visited = set()

        while pq:
            current_dist, current, path_edges, path_nodes = heappop(pq)

            if current in visited:
                continue
            visited.add(current)
                
            if current == goal:
                print("STOP")
            
        


        




    def bfs(self, start_name, goal_name):
        for edge in self.edges:
            edge.update_state()
        start = next((n for n in self.nodes if n.text == start_name), None)
        goal = next((n for n in self.nodes if n.text == goal_name), None)

        if not start or not goal:
            messagebox.showerror("Invalid", "Start or goal node not found.")
            return

        visited = set()
        queue = [(start, [],[start])]  # Each item: (current_node, path_edges)

        while queue:
            current, path_edges, path_nodes = queue.pop(0)
            if current in visited:
                continue
            visited.add(current)

            self.canvas.update()
            self.canvas.after(100)

            if current == goal:
                total_distance = sum(edge.distance for edge in path_edges)
                total_time = sum(edge.time for edge in path_edges)
                for edge in path_edges:
                    self.canvas.itemconfig(edge.line, fill="green")
                self.display_output(
                    f"Path: {' → '.join(n.text for n in path_nodes)}\n"
                    f"Length: {len(path_edges)} edges\n"
                    f"Total Distance: {total_distance}m\n"
                    f"Total Time: {total_time}min")
                return

            for edge in self.get_connected_edges(current):
                neighbor = edge.second_node if edge.first_node == current else edge.first_node
                if neighbor not in visited:
                    queue.append((neighbor, path_edges + [edge], path_nodes + [neighbor]))

        messagebox.showinfo("No Path", "No path found.")


    def get_neighbors(self,node):
        neighbors = []
        for edge in self.edges:
            if not edge.open:
                continue
            if self.accessible_only_mode.get() and not edge.accessible:
                continue
            if edge.first_node == node:
                neighbors.append(edge.second_node)
            elif edge.second_node == node:
                neighbors.append(edge.first_node)

        return neighbors
    
    def get_connected_edges(self, node):
        edges = []
        for edge in self.edges:
            if not edge.open:
                continue
            if self.accessible_only_mode.get() and not edge.accessible:
                continue
            if edge.first_node == node or edge.second_node == node:
                edges.append(edge)
        return edges
class Edge:
    def __init__(self, canvas, first_node, second_node, distance, time, accessible= True, open=True):
        self.selected= False
        self.canvas = canvas
        self.first_node = first_node
        self.second_node = second_node
        self.distance = distance
        self.time = time
        self.accessible = accessible
        self.open = open


        self.line = self.canvas.create_line(first_node.x, first_node.y, second_node.x, second_node.y, fill="blue", width=3)
        self.label = self.canvas.create_text(
            (first_node.x + second_node.x) // 2,
            (first_node.y + second_node.y) // 2 - 10,
            text=f"{distance}m, {time}min",fill="white",font=(("Helvetica", 10, "bold"))
        )
        self.canvas.tag_bind(self.line,"<Button-1>",self.on_left_click)

       
        print("EDGE CREATED, accesible = :",self.accessible)
        
    def update_state(self):
        if not self.open:
            color ="red"
        elif not self.accessible:
            color = "orange"
        else:
            color = "black"
        self.canvas.itemconfig(self.line, fill=color)

    def toggle_open(self):
        self.open = not self.open
        self.update_state()

    def on_left_click(self,event):
        menu = Menu(self.canvas,tearoff=0)
        menu.add_command(label="Toggle Open/Closed", command=self.toggle_open)
        menu.tk_popup(event.x_root,event.y_root)

class Node:
    def __init__(self, canvas, x, y, text="Node", manager=None):
        self.selected = False
        self.canvas = canvas
        self.x = x
        self.y = y
        self.text = text
        self.original_color = random.choice(tk_colors)
        self.rect = self.canvas.create_rectangle(x-50, y-20, x+50, y+20, fill=(self.original_color),tags="node")
        self.text_item = self.canvas.create_text(x, y, text=text,font=("Helvetica", 12, "bold"),tags="node")

        
        self.manager = manager
        self.canvas.tag_bind(self.rect,"<Button-1>",self.on_click)


        #debug 
        print("Node created with color", self.original_color)

    def on_click(self,event):
        if not self.selected: # if its not currently selected 
            print(f"{self.text} is now selected.")
            self.selected = True
            self.canvas.itemconfig(self.rect, fill="lightgreen")
            self.manager.select(self)
        else:
            print(f"{self.text} is now unselected")
            self.selected = False
            self.canvas.itemconfig(self.rect, fill=self.original_color)
            self.manager.deselect(self)

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

if __name__ == "__main__":
    create_nodes_on_canvas()
