from tkinter import *

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