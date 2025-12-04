import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk
from backend.campus_navigator.node_manager import NodeManager
from backend.campus_navigator import ui_helpers
from backend.algo_info import create_nodes

from winsound import *
#sounds
import winsound

import os



class Sidebar(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, width=185, height=720, bg="#0B1D3A", **kwargs)
        self.pack(side=tk.LEFT)
        self.pack_propagate(False)
        
        #STATES
        self.states = ["CAMPUS_NAVIGATOR","STUDY_PLANNER","NOTES_SEARCH","ALGO_INFO"]


        #colors
        self.FRAME_COLOR = "#0B1D3A"
        self.TEXT_COLOR = "white"
        self.FADE_COLOR = '#182F53'

        # Fonts
        self.title_font = tkFont.Font(family="Museo Sans 900", size=18, weight="bold")
        self.middle_font = tkFont.Font(family="Museo Sans 700", size=16, weight="bold")
        self.small_font = tkFont.Font(family="Museo Sans 100", size=10)
        

        # Title
        app_title = tk.Label(self, text="Titan Campus\nAlgorithmic\nAssistant",
                             font=self.title_font, bg=self.FRAME_COLOR, fg="white", justify="left")
        app_title.pack(anchor="nw", padx=10, pady=10)

        # Subtitle
        small_title = tk.Label(self, text="CSUF Algorithm Program",
                               font=self.small_font, bg="#0B1D3A", fg="white")
        small_title.pack(anchor="nw", padx=10, pady=2)

        # Divider
        divider = tk.Frame(self, bg="gray", height=1, width=185)
        divider.pack(anchor="nw", pady=(0, 10))

        # Load icons and keep references in instance variables
        self.info_icon = self.resize_image(
            "gui/build/assets/frame0/info.png"
        )
        self.calendar_icon = self.resize_image(
            "gui/build/assets/frame0/calendar.png"
        )
        
        self.search_icon = self.resize_image("gui/build/assets/frame0/search (2).png")

        self.campus_icon = self.resize_image("gui/build/assets/frame0/map-marker.png")

        self.csuf_icon = self.resize_image("gui/build/assets/frame0/California_State_University,_Fullerton_seal.svg.png",(95,95))
        # Buttons with icons

        campus_nav_btn = tk.Button(self, text="Campus \nNavigator", image=self.campus_icon,
                                 compound="left", bg=self.FRAME_COLOR, fg="white", 
                                 relief="flat", padx=10, anchor="w",font=self.middle_font,command=self.master.content.show_navigation)
        campus_nav_btn.pack(anchor="nw", padx=20, pady=15, fill="x")

        campus_nav_btn.bind("<Enter>", self.on_enter)
        campus_nav_btn.bind("<Leave>", self.on_leave)

        study_planner_btn = tk.Button(self, text="Study\nPlanner", image=self.calendar_icon,
                                 compound="left", bg=self.FRAME_COLOR, fg="white", 
                                 relief="flat", padx=10, anchor="w",font=self.middle_font, command=self.master.content.show_planner)
        study_planner_btn.pack(anchor="nw", padx=20, pady=15, fill="x")

        study_planner_btn.bind("<Enter>", self.on_enter)
        study_planner_btn.bind("<Leave>", self.on_leave)


        notes_search_btn = tk.Button(self, text=" Notes \nSearch", image=self.search_icon,
                               compound="left", bg=self.FRAME_COLOR, fg="white", 
                               relief="flat", padx=10, anchor="w",font=self.middle_font,command=self.master.content.show_notes_search)
        notes_search_btn.pack(anchor="nw", padx=20, pady=15, fill="x")

        notes_search_btn.bind("<Enter>", self.on_enter)
        notes_search_btn.bind("<Leave>", self.on_leave)


        algo_info_btn = tk.Button(self, text=" Algo\nInfo", image=self.info_icon,
                               compound="left", bg=self.FRAME_COLOR, fg="white", 
                               relief="flat", padx=10, anchor="w",font=self.middle_font, command=self.master.content.show_algo_info)
        algo_info_btn.pack(anchor="nw", padx=20, pady=15, fill="x")

        algo_info_btn.bind("<Enter>", self.on_enter)
        algo_info_btn.bind("<Leave>", self.on_leave)

        divider = tk.Frame(self, bg="gray", height=1, width=185)
        divider.pack(anchor="nw", pady=(40, 10))

        image = self.csuf_icon
        image_label = tk.Label(self, image=image,bg=self.FRAME_COLOR)
        image_label.pack(pady=(10,10))

    def on_enter(self,e):
        e.widget['bg'] = self.FADE_COLOR
        e.widget['cursor'] = "hand2"
        self.play_hover_sound()
        
    def play_hover_sound(self):
        winsound.PlaySound(
            "gui/build/assets/sounds/blipSelect.wav",
            winsound.SND_FILENAME | winsound.SND_ASYNC
        )

    def on_leave(self,e):
        e.widget["bg"] = self.FRAME_COLOR
        

    def resize_image(self, png_file, size=(20, 20)):
        try:
            temp = Image.open(png_file)
            temp = temp.resize(size, Image.Resampling.LANCZOS)
            resized_image = ImageTk.PhotoImage(temp)
            return resized_image
        except Exception as e:
            print(f"Image load error: {png_file}, {e}")
            return None
        
    #functions

    # def show_nav(self):
    #     self.master.content.update_view("Campus Navigator")
    # def show_algo(self):
    #     self.master.content.update_view("ALgorithm Info Page")

    

    #problem i faced. I had functions resize_image outside the sidebar scope which dont work as its not returning the resized images.
class Content(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, width=1095, height=720, bg="#E5D9D9", **kwargs)
        self.pack(side=tk.RIGHT, fill="both", expand=True)

        bg_img = Image.open("gui/build/assets/frame0/fall-vector.png")
        bg_img = bg_img.resize((1095,720))

        self.bg_photo = ImageTk.PhotoImage(bg_img)
         #colors
        self.FRAME_COLOR = "#0B1D3A"
        self.TEXT_COLOR = "white"
        self.FADE_COLOR = '#182F53'

        # Fonts
        self.title_font = tkFont.Font(family="Museo Sans 900", size=18, weight="bold")
        self.middle_font = tkFont.Font(family="Museo Sans 700", size=16, weight="bold")
        self.small_font = tkFont.Font(family="Museo Sans 100", size=10)
    
        """ HEADER """
        # self.header = tk.Frame(self, bg=self.FADE_COLOR, height=50)
        # self.header.pack(side="top",fill="x")

        # self.body = tk.Frame(self, bg=self.FADE_COLOR)
        # self.body.pack(side="top",fill="both",expand=True)
        """ BODY """
        self.body = tk.Canvas(self, width=1095, height=720,highlightthickness=0,bd=0)
        self.body.pack(side="top", fill="both", expand=True)
        self.body.create_image(0, 0, image=self.bg_photo, anchor="nw")


        # self.content_title = tk.Label(self.header, text="Main Content Area",bg=self.FADE_COLOR,font=self.title_font,fg="white")
        # self.content_title.pack(side="top")

       
    def clear_body(self):
        for widget in self.body.winfo_children():
            widget.destroy()

    def set_title(self,text):
        self.content_title.config(text=text)

    def show_navigation(self):
        self.clear_body()
        # self.set_title("Campus Navigator")

        ui_helpers.create_nodes_ui(self.body,self.FRAME_COLOR,small_font=self.small_font)

    def show_planner(self):
        self.clear_body()
    def show_notes_search(self):
        self.clear_body()
    def show_algo_info(self):
        self.clear_body()
        create_nodes.create_nodes_ui_algo(self.body, self.FRAME_COLOR,small_font=self.middle_font)
    

    # def update_view(self, text):
    #     # Clear existing widgets
    #     for widget in self.winfo_children():
    #         widget.destroy()

    #     # Add a new label
    #     tk.Label(self, text=text, bg="#E5D9D9", font=("Arial", 18, "bold")).pack(pady=20)

    #     # Add something else (example: a button)
    #     tk.Button(self, text="Do Something", command=lambda: print("Button clicked")).pack(pady=10)

    #     # Add another widget (example: an entry box)
    #     tk.Entry(self).pack(pady=10)
    


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("TCAA")
        self.resizable(False, False)
        self.geometry("1280x720")
        #initializa pygame

        
        # Build layout

        self.content = Content(self)
        self.sidebar = Sidebar(self)

if __name__ == "__main__":
    app = App()
    app.mainloop()