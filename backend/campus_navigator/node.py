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
import random


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