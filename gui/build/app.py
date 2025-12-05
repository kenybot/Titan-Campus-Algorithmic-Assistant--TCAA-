import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk

from backend.campus_navigator import ui_helpers
from backend.algo_info import create_nodes
from backend.study_planner import create_planner
from backend.home import home
from winsound import *
#sounds
import winsound
import time
import os


class Sidebar(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, width=185, height=720, bg="#0B1D3A", **kwargs)
        self.pack(side=tk.LEFT)
        self.pack_propagate(False)
        self.active_btn = None
        
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
                                 relief="flat", padx=10, anchor="w",font=self.middle_font,command=self.master.content.show_navigation, activebackground=self.FADE_COLOR,activeforeground="white")
        campus_nav_btn.pack(anchor="nw", padx=20, pady=15, fill="x")

        campus_nav_btn.bind("<Enter>", self.on_enter)
        campus_nav_btn.bind("<Leave>", self.on_leave)
        campus_nav_btn.bind("<Button-1>" ,self.on_click)

        study_planner_btn = tk.Button(self, text="Study\nPlanner", image=self.calendar_icon,
                                 compound="left", bg=self.FRAME_COLOR, fg="white", 
                                 relief="flat", padx=10, anchor="w",font=self.middle_font, command=self.master.content.show_planner, activebackground=self.FADE_COLOR,activeforeground="white")
        study_planner_btn.pack(anchor="nw", padx=20, pady=15, fill="x")

        study_planner_btn.bind("<Enter>", self.on_enter)
        study_planner_btn.bind("<Leave>", self.on_leave)
        study_planner_btn.bind("<Button-1>" ,self.on_click)


        notes_search_btn = tk.Button(self, text=" Notes \nSearch", image=self.search_icon,
                               compound="left", bg=self.FRAME_COLOR, fg="white", 
                               relief="flat", padx=10, anchor="w",font=self.middle_font,command=self.master.content.show_notes_search, activebackground=self.FADE_COLOR,activeforeground="white")
        notes_search_btn.pack(anchor="nw", padx=20, pady=15, fill="x")

        notes_search_btn.bind("<Enter>", self.on_enter)
        notes_search_btn.bind("<Leave>", self.on_leave)
        notes_search_btn.bind("<Button-1>" ,self.on_click)


        algo_info_btn = tk.Button(self, text=" Algo\nInfo", image=self.info_icon,
                               compound="left", bg=self.FRAME_COLOR, fg="white", 
                               relief="flat", padx=10, anchor="w",font=self.middle_font, command=self.master.content.show_algo_info, activebackground=self.FADE_COLOR,activeforeground="white")
        algo_info_btn.pack(anchor="nw", padx=20, pady=15, fill="x")

        algo_info_btn.bind("<Enter>", self.on_enter)
        algo_info_btn.bind("<Leave>", self.on_leave)
        algo_info_btn.bind("<Button-1>" ,self.on_click)

        divider = tk.Frame(self, bg="gray", height=1, width=185)
        divider.pack(anchor="nw", pady=(40, 10))

        home_btn = tk.Button(self,image= self.csuf_icon,bg=self.FRAME_COLOR, command=self.master.content.show_home,bd=0, activebackground=self.FADE_COLOR,activeforeground="white")
        home_btn.pack(pady=(10,10))

        home_btn.bind("<Enter>",self.on_enter)
        home_btn.bind("<Leave>", self.on_leave)
    
    #HELPER FUNCTIONS FOR SIDEBAR

    def on_enter(self,e):
        e.widget['bg'] = self.FADE_COLOR
        e.widget['cursor'] = "hand2"
        # self.play_hover_sound()

    def on_click(self, e):
        if self.active_btn and self.active_btn != e.widget:
            self.active_btn['bg'] = self.FRAME_COLOR

        # Set new active button
        self.active_btn = e.widget
        self.active_btn['bg'] = self.FADE_COLOR

        
    def play_hover_sound(self):
        winsound.PlaySound(
            "gui/build/assets/sounds/blipSelect.wav",
            winsound.SND_FILENAME | winsound.SND_ASYNC
        )

    def on_leave(self,e):
        if e.widget != self.active_btn:
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
        self.FADE_COLOR = '#182F53'
        self.WHITE_COLOR = "#E5D9D9"

        # Fonts
        self.clock_font = tkFont.Font(family="Museo Sans 900", size=50, weight="bold")
        self.title_font = tkFont.Font(family="Museo Sans 900", size=18, weight="bold")
        self.middle_font = tkFont.Font(family="Museo Sans 700", size=16, weight="bold")
        self.small_font = tkFont.Font(family="Museo Sans 100", size=10)
    
        """ BODY """
        self.body = tk.Canvas(self, width=1095, height=720,highlightthickness=0,bd=0)
        self.body.pack(side="top", fill="both", expand=True)
        self.body.create_image(0, 0, image=self.bg_photo, anchor="nw")

    #HELPER FUNCTIONS FOR CONTENT
    def clear_body(self):
        for widget in self.body.winfo_children():
            widget.destroy()

    def set_title(self,text):
        self.content_title.config(text=text)

    def show_navigation(self):
        self.clear_body()
        ui_helpers.create_nodes_ui(self.body,self.FADE_COLOR,small_font=self.small_font)
        print("moved to navigation")
    def show_planner(self):
        self.clear_body()
        create_planner.create_nodes_ui_planner(self.body)
        print("moved to planner")
    def show_notes_search(self):
        self.clear_body()
        print("moved to notes_search")
    def show_algo_info(self):
        self.clear_body()
        create_nodes.create_nodes_ui_algo(self.body)
        print("moved to algo info")
    def show_home(self):
        self.clear_body()
        home.create_home_ui(self.body, self.FRAME_COLOR, self.clock_font)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("TCAA")
        self.resizable(False, False)
        self.geometry("1280x720")
        self.configure(bg="#0B1D3A")
       
        # Build layout

        self.content = Content(self)
        self.sidebar = Sidebar(self)

if __name__ == "__main__":
    app = App()
    app.mainloop()